from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('buy/<int:id>/',
         views.create_checkout_session,
         name='create_checkout_session'),
    path('item/<int:id>/',
         views.item_info,
         name='item_info'),
    path('success/',
         views.SuccessView.as_view(),
         name='success_page'),
    path('cancelled/',
         views.CancelledView.as_view(),
         name='cancelled_page'),
]
