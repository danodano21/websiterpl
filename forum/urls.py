from django.conf.urls import url

from . import views

urlpatterns = [
        #Leave as empty string for base url

	url(r'^post/(?P<slugInput>[\w-]+)/$', views.detailPost),
	url(r'^$', views.forum,name="forum"),


]
