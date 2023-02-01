from django.urls import path
from .views import OrderListView, InterfaceView

urlpatterns = [
    path('', OrderListView.as_view(), name='waiter_interface'),
    path('order_detail/<uuid:pk>', InterfaceView.as_view(), name='order_detail'),
]
