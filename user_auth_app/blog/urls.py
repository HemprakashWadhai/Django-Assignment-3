from django.urls import path
from .views import create_blog_post, my_blog_posts, blog_list

urlpatterns = [
    path('create/', create_blog_post, name='create_blog_post'),
    path('my-blogs/', my_blog_posts, name='my_blog_posts'),
    path('list/', blog_list, name='blog_list'),
]
