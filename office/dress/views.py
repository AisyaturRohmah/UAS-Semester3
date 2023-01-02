from django.shortcuts import render
from .models import Post

def index(request):
    posts = Post.objects.all()
    context = {
        'title' : ' dress',
        'posts' : posts,
     }

    return render(request, 'indexhtml/dress.html', context)
