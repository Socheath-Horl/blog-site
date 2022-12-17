from django.http import Http404
from django.shortcuts import render, get_object_or_404

from .models import Post


def post_list(request):
    posts = Post.published.all()
    return render(
        request=request, 
        template_name='blog/post/list.xhtml',
        context={'posts': posts}
    )

def post_detail(request, year, month, day, post):
    post = get_object_or_404(
        Post,
        slug=post,
        publish__year=year,
        publish__month=month,
        publish__day=day
    )
    
    return render(
        request=request,
        template_name='blog/post/detail.xhtml',
        context={'post': post}
    )
