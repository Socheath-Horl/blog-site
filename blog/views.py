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

def post_detail(request, id):
    try:
        post = get_object_or_404(
            Post,
            id=id,
            status=Post.Status.PUBLISHED
        )
    except Post.DoesNotExist:
        raise Http404("No Post found.")
    
    return render(
        request=request,
        template_name='blog/post/detail.xhtml',
        context={'post': post}
    )
