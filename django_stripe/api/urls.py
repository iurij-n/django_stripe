from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('buy/<int:id>/', views.buy_item),
    path('item/<int:id>/', views.ItemInfo.as_view(), name='item_info'),
] 