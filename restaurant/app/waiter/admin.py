from django.contrib import admin
from .models import Waiter


@admin.register(Waiter)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id",)
