import stripe
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import TemplateView

from .models import Item


def buy_item(request, id):
    return HttpResponse(f'Покупка товара {id}')


stripe.api_key = settings.STRIPE_SECRET_KEY


@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLIC_KEY}
        return JsonResponse(stripe_config, safe=False)


@csrf_exempt
def create_checkout_session(request, id):

    item = get_object_or_404(Item, pk=id)

    session = stripe.checkout.Session.create(
        line_items=[{
            'price_data': {
                'currency': 'rub',
                'product_data': {
                    'name': item.name,
                    },
                'unit_amount': item.price,
            },
            'quantity': 1,
            }],
        mode='payment',
        success_url='http://localhost:8000/success',
        cancel_url='http://localhost:8000/cancel',
    )

    return JsonResponse({'sessionId': session.id})


def item_info(request, id):
    item = get_object_or_404(Item, pk=id)
    context = {
        'item': item,
        'price': f'{item.price/100:.2f}'
    }
    return render(request, 'item_info.html', context)


class SuccessView(TemplateView):
    template_name = 'success.html'


class CancelledView(TemplateView):
    template_name = 'cancelled.html'


def index(request):
    template = 'index.html'
    items = Item.objects.all()
    title = 'Список товаров в магазине'
    context = {
        'items': items,
        'title': title,
    }
    return render(request, template, context)
