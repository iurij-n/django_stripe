from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView


def buy_item(request, id):
    return HttpResponse(f'Покупка товара {id}')


class ItemInfo(TemplateView):
    template_name = 'item_info.html'

def item_info(request, id):
    return HttpResponse(f'Информация о товаре {id}')


def index(request):
    return HttpResponse('Главная страница')
