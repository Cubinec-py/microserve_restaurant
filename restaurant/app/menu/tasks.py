import requests
import os
from urllib.parse import urlparse
from celery import shared_task
from app.menu.models import Dish, CategoryDish
from django.core.files.base import ContentFile


@shared_task
def create_update_dish():
    url = 'http://storehouse:8001/api/dishes/'
    page = ''
    token_value = os.environ.get('TOKEN_VALUE')

    while True:
        try:
            base = requests.get(url + page, headers={'Authorization': f'Token {token_value}'})
        except requests.exceptions.ConnectionError:
            return 'No connection'
        body = base.json()

        try:
            for elements in body['results']:
                if not Dish.objects.filter(id=elements['id']).exists():
                    img_url = elements['image']
                    dish_name = urlparse(img_url).path.split('/')[-1]

                    response = requests.get(img_url)
                    dish = Dish.objects.create(
                        id=elements['id'],
                        name=elements['name'],
                        price=elements['price'],
                        description=elements['description'],
                        amount=elements['amount'],
                        weight=elements['weight'],
                    )
                    for item in elements['category_list']:
                        category_img_ur = elements['image']
                        category_name = urlparse(category_img_ur).path.split('/')[-1]
                        category = CategoryDish.objects.get_or_create(name=item['name'])
                        response_url = requests.get(img_url)
                        dish.category.add(category[0].id)
                        if not category[0].image:
                            category[0].image.save(category_name, ContentFile(response_url.content), save=True)
                    dish.image.save(dish_name, ContentFile(response.content), save=True)
                    dish.save()
        except Exception as e:
            return e

        try:
            page = body['next'].split('/')[-1]
        except AttributeError:
            return 'All updated'
