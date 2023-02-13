from rest_framework import viewsets
from rest_framework import permissions
from .serializers import DishSerializer, CategoryDishSerializer
from .models import Dish, CategoryDish


class DishViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Dish.objects.all().order_by("-id")
    serializer_class = DishSerializer
    permission_classes = [permissions.IsAuthenticated]


class CategoryDishViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = CategoryDish.objects.all().order_by("-id")
    serializer_class = CategoryDishSerializer
    permission_classes = [permissions.IsAuthenticated]
