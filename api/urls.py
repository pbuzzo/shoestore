from django.conf.urls import include, url
from api.views import (
    ShoeViewSet,
    ShoeTypeViewSet,
    ShoeColorViewSet,
    ManufacturerViewSet
)
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'shoe', ShoeViewSet, basename='shoe')
router.register(r'shoecolor', ShoeColorViewSet, basename='shoecolor')
router.register(r'shoetype', ShoeTypeViewSet, basename='shoetype')
router.register(r'manufacturer', ManufacturerViewSet, basename='manufacturer')

urlpatterns = [
    url(r'^api/', include(router.urls))
]