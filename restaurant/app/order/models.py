import uuid

from django.db import models
from app.menu.models import Dish
from app.waiter.models import Waiter
from django.db.models import Sum


class Rating(models.Model):
    rating = models.IntegerField(default=0)


class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Table(models.Model):
    category_hall = (
        ('Зал 1', 'Зал 1'),
        ('Зал 2', 'Зал 2'),
        ('Зал 3', 'Зал 3'),
        ('Терраса', 'Терраса'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    number = models.IntegerField(default=0)
    hall = models.CharField(max_length=100, choices=category_hall, default='Зал 1')
    places_amount = models.IntegerField(default=0, null=True)

    def __str__(self):
        return f'{self.hall}'


class Order(models.Model):
    category_status = (
        ('Готовится', 'Готовится'),
        ('Блюда в зале', 'Блюда в зале'),
        ('Ожидает оплату', 'Ожидает оплату'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order_number = models.IntegerField(default=1)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100, choices=category_status, default='Зал 1')
    waiter = models.ForeignKey(Waiter, on_delete=models.SET_NULL, null=True, blank=True)
    table = models.ForeignKey(Table, on_delete=models.SET_NULL, null=True, blank=True)
    total_payment = models.IntegerField(default=0)
    rating = models.ForeignKey(Rating, on_delete=models.SET_NULL, null=True, blank=True)

    def get_all_status(self):
        return self.category_status

    def save(self, *args, **kwargs):
        if self._state.adding:
            last_id = Order.objects.all().aggregate(largest=models.Max('order_number'))['largest']
            if last_id is not None:
                self.order_number = last_id + 1
        super(Order, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-date_ordered']

    def __str__(self):
        return f'Заказ: {self.id}'


class OrderItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    dish = models.ForeignKey(Dish, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(default=0, null=True)

    def get_total(self):
        return self.quantity * self.dish.price
