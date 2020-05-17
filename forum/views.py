from django.shortcuts import render

# Create your views here.

from .models import Post

def forum(request):
     # queryset
     posts = Post.objects.all();
     context = {
          'title':'Orplant Forum',
          'Posts':posts,
     }
     return render(request, 'forum/index.html', context)

def detailPost(request,slugInput):
     posts = Post.objects.get(slug=slugInput);
     context = {
          'title':'Orplant Forum',
          'Posts':posts,
     }

     return render(request,'forum/detail.html',context)