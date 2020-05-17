from django.conf.urls import url,include
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^artikel/', include('artikel.urls', namespace='artikel')),
    url(r'^store/', include('store.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),

    
    
]
