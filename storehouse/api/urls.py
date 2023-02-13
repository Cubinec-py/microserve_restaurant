from django.urls import include, path
from rest_framework import routers
from products.views import DishViewSet, CategoryDishViewSet
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.authtoken import views

router = routers.DefaultRouter()
router.register(r"dishes", DishViewSet, basename="dish")
router.register(r"category_dish", CategoryDishViewSet, basename="categorydish")

urlpatterns = [
    path(
        "schema/",
        SpectacularAPIView.as_view(custom_settings={"COMPONENT_SPLIT_REQUEST": True}),
        name="schema",
    ),
    path(
        "schema/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path("", include(router.urls)),
    path("registration/", include("dj_rest_auth.registration.urls")),
    path("auth/auth-token", views.obtain_auth_token),
]
