from django.urls import path
from .views import OrderDetailView

urlpatterns = [
    path('order_confirm/<uuid:pk>', OrderDetailView.as_view(), name='order_confirm')
]
