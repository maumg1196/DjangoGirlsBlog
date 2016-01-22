from django.shortcuts import render
from blog.models import Post
from django.utils import timezone


def post_list(request):
    posts = Post.objects.filter(published=timezone.now()).order_by('published')
    return render(request, 'blog/post_list.html', {'posts': posts})
