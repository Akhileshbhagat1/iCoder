from django.shortcuts import render, HttpResponse
from .models import Post


def BlogHome(request):
    allPosts = Post.objects.all()
    context = {'allPosts': allPosts}
    return render(request, 'blog/blogHome.html', context)


def BlogPost(request, slug):
    post = Post.objects.filter(slug=slug).first()
    # print(post)
    context = {'post': post}
    return render(request, 'blog/blogPost.html', context)



