import stripe
from cart.forms import CartAddProductForm
from .forms import CurrencySelectForm
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.views.generic.base import TemplateView

from .models import Item, Сurrency


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
    currency = get_object_or_404(Сurrency,
                                 alphabetic_code=request.session['currency'])

    session = stripe.checkout.Session.create(
        line_items=[{
            'price_data': {
                'currency': currency.alphabetic_code,
                'product_data': {
                    'name': item.name,
                    },
                'unit_amount': int(item.price/currency.exchange_rate),
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
    currency = get_object_or_404(Сurrency,
                                 alphabetic_code=request.session['currency'])
    cart_product_form = CartAddProductForm()
    price = int(item.price/currency.exchange_rate)
    context = {
        'item': item,
        'cart_product_form': cart_product_form,
        'price': f'{price/100:.2f}',
        'currency_symbol': currency.currency_symbol
    }
    return render(request, 'item_info.html', context)


class SuccessView(TemplateView):
    template_name = 'success.html'


class CancelledView(TemplateView):
    template_name = 'cancelled.html'


def index(request):
    template = 'index.html'
    items = Item.objects.all()
    currency = get_object_or_404(Сurrency,
                                 pk=1)
    title = 'Список товаров в магазине'
    if request.session.get('currency'):
        currency_select_form = CurrencySelectForm(
            initial={'currency': request.session['currency']})
    else:
        request.session['currency'] = currency.alphabetic_code
        currency_select_form = CurrencySelectForm()
    context = {
        'items': items,
        'title': title,
        'currency_select_form': currency_select_form,
    }
    return render(request, template, context)


@require_POST
def currency_select(request):
    form = CurrencySelectForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        request.session['currency'] = cd['currency']
    return redirect('api:home_page')
