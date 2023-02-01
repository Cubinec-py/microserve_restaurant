from django.contrib import admin
from .models import Dish, CategoryDish


# class CategoryInline(TabularInline):
#     model = CategoryMenu
#     extra = 1


@admin.register(Dish)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description', 'amount', 'weight')


@admin.register(CategoryDish)
class CategoryMenuAdmin(admin.ModelAdmin):
    list_display = ('name',)
