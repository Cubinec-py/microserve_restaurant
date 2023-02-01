from django.urls import path
from .views import cart, process_order

urlpatterns = [
    path('', cart, name='cart'),
    path('cart_apply/', process_order, name='cart_apply'),
]
