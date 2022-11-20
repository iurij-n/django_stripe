import stripe
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic.base import TemplateView

from .models import Item


def buy_item(request, id):
    return HttpResponse(f'Покупка товара {id}')


stripe.api_key = 'sk_test_51M5uagFXiDYe7Pq7YMLy1yO1HS0Rt5AwxK2jtTUqyZh6YRJ1FTukYMwPDApSMJPka9PDC1qq6d2HO2OxIntTCukt00wOVIPLwO'

def create_checkout_session(request, id):
    
    item=get_object_or_404(Item, pk=id)
    
    session = stripe.checkout.Session.create(
        line_items=[{
        'price_data': {
            'currency': 'usd',
            'product_data': {
            'name': item.name,
            },
            'unit_amount': item.price,
        },
        'quantity': 1,
        }],
        mode='payment',
        success_url='http://127.0.0.1:8000/success',
        cancel_url='http://127.0.0.1:80002/cancel',
    )

    return JsonResponse({'sessionId': session.id})


class ItemInfo(TemplateView):
    template_name = 'item_info.html'

def item_info(request, id):
    # item = Item.objects.get(pk=id)
    item = get_object_or_404(Item, pk=id)
    context = {
        'item': item,
    }
    return render(request, 'item_info.html', context)


class SuccessView(TemplateView):
    template_name = 'success.html'


class CancelledView(TemplateView):
    template_name = 'cancelled.html'


def index(request):
    return HttpResponse('Главная страница')
