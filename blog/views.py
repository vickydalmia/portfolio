from django.shortcuts import render, get_object_or_404
from .models import BlogPost

# Create your views here.
def blogHome(request):
    posts = BlogPost.objects
    return render(request, 'blogs/allblog.html', {'posts': posts})


def blogDetail(request, blog_id):
    post = get_object_or_404(BlogPost, pk=blog_id)
    return render(request, 'blogs/postdetail.html', {'post': post})
