from decimal import Decimal

from api.models import Item
from coupon.models import Coupon
from django.conf import settings


class Cart(object):

    def __init__(self, request):
        """
        Инициализируем корзину
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart
        self.coupon_id = self.session.get('coupon_id')

    def add(self, item, quantity=1, update_quantity=False):
        """
        Добавить продукт в корзину или обновить его количество.
        """
        item_id = str(item.id)
        if item_id not in self.cart:
            self.cart[item_id] = {'quantity': 0,
                                  'price': str(item.price),
                                  'fprice': f'{item.price/100:.2f}'}
        if update_quantity:
            self.cart[item_id]['quantity'] = quantity
        else:
            self.cart[item_id]['quantity'] += quantity
        self.save()

    def save(self):
        # Обновление сессии cart
        self.session[settings.CART_SESSION_ID] = self.cart
        # Отметить сеанс как "измененный", чтобы убедиться, что он сохранен
        self.session.modified = True

    def remove(self, item):
        """
        Удаление товара из корзины.
        """
        item_id = str(item.id)
        if item_id in self.cart:
            del self.cart[item_id]
            self.save()

    def __iter__(self):
        """
        Перебор элементов в корзине и получение продуктов из базы данных.
        """
        item_ids = self.cart.keys()
        # получение объектов item и добавление их в корзину
        items = Item.objects.filter(id__in=item_ids)
        for item in items:
            self.cart[str(item.id)]['item'] = item

        for catr_item in self.cart.values():
            catr_item['price'] = Decimal(catr_item['price'])
            catr_item['total_price'] = (
                catr_item['price'] * catr_item['quantity'])
            total_price = catr_item['total_price']
            catr_item['total_price'] = f'{total_price/100:.2f}'
            yield catr_item

    def __len__(self):
        """
        Подсчет всех товаров в корзине.
        """
        return sum(
            catr_item['quantity'] for catr_item in self.cart.values())

    def get_total_price(self):
        """
        Подсчет стоимости товаров в корзине.
        """
        total_cart_price = sum((Decimal(catr_item['price'])) *
                               catr_item['quantity'] for catr_item in
                               self.cart.values())
        return f'{total_cart_price/100:.2f}'

    def get_total_price_in_cents(self):
        """
        Стоимости товаров в корзине выраженное в копейках.
        """
        return int(sum((Decimal(catr_item['price'])) *
                       catr_item['quantity'] for catr_item in
                       self.cart.values()))

    def clear(self):
        # удаление корзины из сессии
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
    
    @property
    def coupon(self):
        if self.coupon_id:
            return Coupon.objects.get(id=self.coupon_id)
        return None

    def get_discount(self):
        if self.coupon:
            return ((self.coupon.discount / Decimal('100')) *
                    self.get_total_price_in_cents() /
                    100)
        return Decimal('0')

    def get_total_price_after_discount(self):
        return Decimal(self.get_total_price_in_cents()/100)-self.get_discount()
