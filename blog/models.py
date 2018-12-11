from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.html import strip_tags
import markdown

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=70)
    body = models.TextField()
    #创建时间和修改时间
    create_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    #摘要
    excerpt = models.CharField(max_length=200,blank=True)
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag, blank=True)
    author = models.ForeignKey(User)

    views = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.excerpt:
            md = markdown.Markdown(extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
            ])
            #先将MarkDown文本渲染成html文本
            #再用strip_tags去掉Html文本的全部html标签
            #提取前54个字符赋值给excerpt
            self.excerpt = strip_tags(md.convert(self.body))[:54]
        super().save(*args, **kwargs)

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail',kwargs={'pk':self.pk})

    class Meta:
        ordering = ["-create_time"]
