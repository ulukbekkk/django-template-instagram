from django.http import HttpResponse
from django.shortcuts import render
from .models import Post

def index(request):
    post = Post.objects.all()
    return render(request, 'post_list.html', {'post': post})


