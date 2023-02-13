from django.urls import path
from .views import (
    OrderListView,
    InterfaceView,
    TipsDetailView,
    RestaurantStatsDetailView,
)

urlpatterns = [
    path("", OrderListView.as_view(), name="waiter_interface"),
    path("order_detail/<uuid:pk>", InterfaceView.as_view(), name="order_detail"),
    path("waiter_tips/", TipsDetailView.as_view(), name="waiter_tips"),
    path(
        "restaurant_stats/",
        RestaurantStatsDetailView.as_view(),
        name="restaurant_stats",
    ),
]
