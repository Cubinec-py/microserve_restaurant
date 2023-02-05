from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum


class Waiter(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-id']


class Tips(models.Model):
    amount = models.FloatField(default=0, null=True)
    waiter = models.ForeignKey(Waiter, on_delete=models.SET_NULL, null=True, blank=True)
