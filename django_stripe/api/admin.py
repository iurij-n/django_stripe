from django.contrib import admin

from .models import Item, Сurrency


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'description',
                    'price',
                    'image')
    search_fields = ('name',)
    empty_value_display = '-пусто-'
    

class СurrencyAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'alphabetic_code',
                    'currency_symbol',
                    'exchange_rate',)
    search_fields = ('name',)
    empty_value_display = '-пусто-'


admin.site.register(Item, ItemAdmin)
admin.site.register(Сurrency, СurrencyAdmin)
