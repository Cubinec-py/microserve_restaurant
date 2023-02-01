import django_filters
from django_filters import RangeFilter

from .models import Dish


class MenuFilter(django_filters.FilterSet):
    price = RangeFilter()

    class Meta:
        model = Dish
        fields = {
            'price': [],
            'category': ['exact'],
        }
