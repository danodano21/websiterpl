from django.shortcuts import render

def index(request):
     context = {
          'title':'Orplant',

     }
     return render(request, 'index.html', context)


def login(request):
     context = {
          'title':'Orplant',

     }
     return render(request, 'login.html', context)