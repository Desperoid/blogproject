from django.conf.urls import url
from . import views

app_name = 'comments'
urlpatterns = [url(r'^comments/post/(?P<post_pk>\d+)/$', views.post_comments, name = 'post_comments'),]
