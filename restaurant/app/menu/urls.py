from django.urls import path
from .views import ShowMenuListView

urlpatterns = [
    path('', ShowMenuListView.as_view(), name='menu'),
]
