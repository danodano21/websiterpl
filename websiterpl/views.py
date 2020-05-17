from django.shortcuts import render

# Create your views here.
def index(request):
     context = {
          'title':'Orplant',
          'heading':'',
          'subheading':''

     }
     return render(request, 'index.html', context)