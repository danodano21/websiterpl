from django.conf.urls import url

from . import views

urlpatterns = [
        #Leave as empty string for base url
    url(r'^delete/(?P<delete_id>[0-9])/$', views.deletePost, name='delete'),
	url(r'^singlepost/(?P<slugInput>[\w-]+)/$', views.detailPost, name='single'),
	url(r'^create/$', views.createPost, name='create'),
	url(r'^$', views.allPost ,name="allpost"),


]
