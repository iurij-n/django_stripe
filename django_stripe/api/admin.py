from django.contrib import admin
from .models import Item

class ItemAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'description', 'price')
    search_fields = ('name',)
    empty_value_display = '-пусто-'

admin.site.register(Item, ItemAdmin)