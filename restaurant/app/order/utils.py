import json


def cookie_items(request):
    # Create empty cart for now for non-logged in user
    try:
        cart = json.loads(request.COOKIES['cart'])
    except:
        cart = {}
        print('CART:', cart)
    items = {}
    for i in cart:
        try:
            items['first_name'] = cart['first_name']
            items['last_name'] = cart['last_name']
        except:
            pass
    return items
