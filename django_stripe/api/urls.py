from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

app_name = 'api'

urlpatterns = [
     path('', views.index,
          name='home_page'),
     path('config/', views.stripe_config),
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
     path('currency_select/',
          views.currency_select,
          name='currency_select'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
