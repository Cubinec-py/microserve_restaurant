import json

from django.shortcuts import render
from .utils import cart_data
from django.http import JsonResponse
from .utils import guest_order
from app.order.models import Table


def cart(request):
    data = cart_data(request)
    tables = Table.objects.all()

    cart_items = data['cart_items']
    order = data['order']
    items = data['items']

    context = {'items': items, 'order': order, 'cart_items': cart_items, 'tables': tables}
    return render(request, 'cart/cart.html', context)


def process_order(request):
    data = json.loads(request.body)
    guest_order(request, data)

    return JsonResponse('Order complete', safe=False)
