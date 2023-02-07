from django.urls import include, path
from rest_framework import routers
from products import views
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

router = routers.DefaultRouter()
router.register(r'dishes', views.DishViewSet, basename='dish')
router.register(r'category_dish', views.CategoryDishViewSet, basename='categorydish')

urlpatterns = [
    path('schema/', SpectacularAPIView.as_view(custom_settings={"COMPONENT_SPLIT_REQUEST": True}), name='schema'),
    path('schema/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

    path('', include(router.urls)),
]
