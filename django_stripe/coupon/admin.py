from django.conf import settings
from django.contrib import admin

from .models import Coupon


class CouponAdmin(admin.ModelAdmin):
    list_display = ('code',
                    'valid_from',
                    'valid_to',
                    'discount',
                    'active')
    search_fields = ('code',)
    empty_value_display = settings.EMPTY_VALUE_DISPLAY


admin.site.register(Coupon, CouponAdmin)
