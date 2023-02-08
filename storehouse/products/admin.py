from django.contrib import admin
from .models import Dish, CategoryDish


@admin.register(Dish)
class MenuAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "description", "amount", "weight")


@admin.register(CategoryDish)
class CategoryDishAdmin(admin.ModelAdmin):
    list_display = ("name",)
