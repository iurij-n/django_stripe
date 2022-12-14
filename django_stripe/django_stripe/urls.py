# from django.conf import settings
# from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('api.urls')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('coupon/', include('coupon.urls', namespace='coupon')),
    path('admin/', admin.site.urls),
]

# if settings.DEBUG:
#     urlpatterns += static(
#         settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
#     )
