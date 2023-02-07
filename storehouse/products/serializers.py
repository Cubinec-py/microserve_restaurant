from .models import Dish, CategoryDish
from rest_framework import serializers


class DishSerializer(serializers.HyperlinkedModelSerializer):
    category_list = serializers.SerializerMethodField()

    def get_category_list(self, instance):
        data_models = CategoryDish.objects.filter(dish=instance)
        serializer = CategoryDishSerializer(instance=data_models, many=True, read_only=True)

        return serializer.data

    class Meta:
        model = Dish
        fields = ['id', 'name', 'price', 'description', 'amount', 'weight', 'category_list', 'status', 'image']


class CategoryDishSerializer(serializers.ModelSerializer):

    class Meta:
        model = CategoryDish
        fields = ['id', 'name']
