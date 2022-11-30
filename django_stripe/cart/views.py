import stripe
from api.models import Item
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from .cart import Cart
from .forms import CartAddProductForm


@require_POST
def cart_add(request, item_id):
    cart = Cart(request)
    item = get_object_or_404(Item, id=item_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(item=item,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:cart_detail')


def cart_remove(request, item_id):
    cart = Cart(request)
    item = get_object_or_404(Item, id=item_id)
    cart.remove(item)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    context = {
        'cart': cart,
    }
    return render(request, 'cart_detail.html', context)

@csrf_exempt
def create_cart_checkout_session(request):

    cart = Cart(request)

    session = stripe.checkout.Session.create(
        line_items=[{
            'price_data': {
                'currency': 'rub',
                'product_data': {
                    'name': 'Товары из корзины',
                    },
                'unit_amount': cart.get_total_price_in_cents(),
            },
            'quantity': 1,
            }],
        mode='payment',
        success_url='http://localhost:8000/cart/success',
        cancel_url='http://localhost:8000/cancel',
    )

    return JsonResponse({'sessionId': session.id})


def success_view(request):
    cart = Cart(request)
    cart.clear()
    return render(request, 'success.html')
