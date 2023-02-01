from django.contrib import admin
from app.order.models import Table, Order, OrderItem


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('hall', 'number')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'date_ordered', 'status')


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'dish', 'quantity', 'table_item')
