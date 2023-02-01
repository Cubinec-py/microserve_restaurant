import uuid

from django.db import models


class CategoryDish(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='category_dishes', null=True)

    def __str__(self):
        return self.name


class Dish(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(max_length=1000)
    amount = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)
    category = models.ManyToManyField(CategoryDish)
    image = models.ImageField(upload_to='dishes', null=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.name
