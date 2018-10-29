from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from .models import Comment
from blog.models import Post
from .forms import CommentForm

def post_comments(request, post_pk):
    post = get_object_or_404(Post,pk=post_pk)
    print(request.method)
    print(request.method.lower() == 'post')
    if request.method.lower() == 'post':
        form = CommentForm(request.POST)
        print(form)
        print(form.is_valid())
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect(post)
        else :
            comment_list = post.comment_set.all()
            context = {'post':post,
                       'form':form,
                       'coment_list':comment_list,
            }
            return render(request,'blog/detail.html',context=context)
    return redirect(post)
