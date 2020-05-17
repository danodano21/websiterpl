from django.conf.urls import url,include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from . import views
from store import views as storeViews

urlpatterns = [
    url(r'^artikel/', include('artikel.urls', namespace='artikel')),
    url(r'^store/', include('store.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^cart/',include('store.urls')),
    url(r'^checkout/',include('store.urls')),
    url(r'^update_item/$',storeViews.updateItem,name='update_item'),
    url(r'^process_order/$',storeViews.processOrder,name='process_order'),
    
   
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
