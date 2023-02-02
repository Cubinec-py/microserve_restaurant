import json
from app.order.models import Order, OrderItem, Customer, Table
from app.menu.models import Dish
from django.shortcuts import get_object_or_404


def cookie_cart(request):
    # Create empty cart for now for non-logged in user
    try:
        cart = json.loads(request.COOKIES['cart'])
    except:
        cart = {}
        print('CART:', cart)

    items = []
    order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
    cart_items = order['get_cart_items']

    for i in cart:
        # We use try block to prevent items in cart that may have been removed from causing error
        try:
            if (cart[i]['quantity'] > 0):  # items with negative quantity = lot of freebies
                cart_items += cart[i]['quantity']

                dish = Dish.objects.get(id=i)
                total = (dish.price * cart[i]['quantity'])

                order['get_cart_total'] += total
                order['get_cart_items'] += cart[i]['quantity']

                item = {
                    'id': dish.id,
                    'dish': {
                        'id': dish.id,
                        'name': dish.name,
                        'price': dish.price,
                        'description': dish.description,
                        'weight': dish.weight,
                        'category': dish.category,
                        'imageURL': dish.image,
                    }, 'amount': cart[i]['quantity'], 'get_total': total,
                }
                items.append(item)
        except:
            pass
    return {'cart_items': cart_items, 'order': order, 'items': items}


def cart_data(request):
    cookie_data = cookie_cart(request)
    cart_items = cookie_data['cart_items']
    order = cookie_data['order']
    items = cookie_data['items']

    return {'cart_items': cart_items, 'order': order, 'items': items}


def guest_order(request, data):
    first_name = data['form']['first_name']
    last_name = data['form']['last_name']
    table = data['table']['table_id']
    cookie_data = cookie_cart(request)
    items = cookie_data['items']

    customer, created = Customer.objects.get_or_create(
        first_name=first_name,
        last_name=last_name,
    )
    customer.save()

    order = Order.objects.create(
        customer=customer,
        status='Готовится',
        table_id=table,
    )
    for item in items:
        dish = Dish.objects.get(id=item['id'])
        OrderItem.objects.create(
            dish=dish,
            order=order,
            quantity=(item['amount'] if item['amount'] > 0 else -1 * item['amount']),
        )

    return customer, order
