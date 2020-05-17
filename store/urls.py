from django.conf.urls import url

from . import views

urlpatterns = [
        #Leave as empty string for base url

	# path('', views.store, name="store"),
	url(r'^$', views.store, name="store"),
	# path('cart/', views.cart, name="cart"),
	url(r'^cart/$', views.cart, name="cart"),
	# path('checkout/', views.checkout, name="checkout"),
	url(r'^store/$', views.checkout, name="checkout"),

]
