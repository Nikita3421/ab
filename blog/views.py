from django.shortcuts import render
from .models import Post, Author, Comment

def post_list(request):
    posts = Post.objects.all()
    context = {
        "posts_list": posts,
    }
    return render(
        request,
        "blog/post_list.html",
        context=context,
    )

def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    published_recently = post.published_recently()
    context = {
        "post": post,
        "published_recently": published_recently,
        "comments":post.comments.all()
    }
    return render(
        request,
        "blog/post_detail.html",
        context=context,
    )

def author_posts(request, author_id):
    author = Author.objects.get(id=author_id)
    context = {
        "author": author,
        "posts":author.posts.all()
    }
    return render(
        request,
        "blog/author_posts.html",
        context=context,
    )
    