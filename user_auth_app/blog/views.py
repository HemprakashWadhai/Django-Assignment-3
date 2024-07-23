from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import BlogPostForm
from .models import BlogPost

@login_required
def create_blog_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.author = request.user
            blog_post.save()
            return redirect('my_blog_posts')
    else:
        form = BlogPostForm()
    return render(request, 'create_blog_post.html', {'form': form})


@login_required
def my_blog_posts(request):
    posts = BlogPost.objects.filter(author=request.user)
    return render(request, 'my_blog_posts.html', {'posts': posts})

def blog_list(request):
    categories = BlogPost.CATEGORY_CHOICES
    blogs = {category: BlogPost.objects.filter(category=category[0], is_draft=False) for category in categories}
    return render(request, 'blog_list.html', {'blogs': blogs})
