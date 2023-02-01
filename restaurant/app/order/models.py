import uuid

from django.db import models
from app.menu.models import Dish
from app.waiter.models import WaiterItem


class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Tips(models.Model):
    amount = models.FloatField(default=0, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.customer.first_name


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
    waiter = models.ForeignKey(WaiterItem, on_delete=models.SET_NULL, null=True, blank=True)

    def get_all_status(self):
        return self.category_status

    def save(self, *args, **kwargs):
        if self._state.adding:
            last_id = self.objects.all().aggregate(largest=models.Max('order_number'))['largest']
            print(last_id)
            # if last_id is not None:
            #     self.order_number = last_id + 1
        super(Order, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-date_ordered']

    def __str__(self):
        return f'Заказ: {self.id}'


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


class TableItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    table = models.ForeignKey(Table, on_delete=models.SET_NULL, null=True, blank=True)
    is_reserved = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.table} {self.waiter}'


class OrderItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    dish = models.ForeignKey(Dish, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(default=0, null=True)
    tips = models.ForeignKey(Tips, on_delete=models.SET_NULL, null=True, blank=True)
    table_item = models.ForeignKey(TableItem, on_delete=models.SET_NULL, null=True, blank=True)

    def get_total(self):
        return self.quantity * self.dish.price
