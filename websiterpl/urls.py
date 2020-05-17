from django.conf.urls import url,include
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^forum/', include('forum.urls')),
    url(r'^store/', include('store.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),

    
    
]
