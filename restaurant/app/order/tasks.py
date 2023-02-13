import requests
import os
from celery import shared_task
from app.menu.models import Dish
from django.shortcuts import get_object_or_404
from dotenv import load_dotenv

load_dotenv()


@shared_task
def update_dish_amount(dish_id, dish_amount):
    try:
        dish = get_object_or_404(Dish, id=dish_id)
    except Exception as e:
        return e
    dish_elements = {
        'amount': dish.amount
    }
    try:
        token_value = os.environ.get('TOKEN_VALUE')
        requests.patch(
            'http://storehouse:8001/api/dishes/' + dish_amount,
            headers={'Authorization': f'Token {token_value}'},
            json=dish_elements
        )
    except Exception as e:
        return e
