from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    url(r'^$', views.cart_detail, name='cart_detail'),
    url(r'^add/(?P<item_id>\d+)/$', views.cart_add, name='cart_add'),
    url(r'^remove/(?P<item_id>\d+)/$', views.cart_remove, name='cart_remove'),
    path('buy/',
        views.create_cart_checkout_session,
        name='create_cart_checkout_session'),
]