from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import MyLoginView

urlpatterns = [
    path('', MyLoginView.as_view(), name='custom_login'),
    path('logout/', LogoutView.as_view(), name='log_out'),
]
