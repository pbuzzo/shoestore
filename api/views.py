from django.shortcuts import render
from api.serializer import (
    ShoeSerializer,
    ShoeTypeSerializer,
    ShoeColorSerializer,
    ManufacturerSerializer
)
from shoeapp.models import (
    Shoe,
    ShoeType,
    ShoeColor,
    Manufacturer
)
from rest_framework.viewsets import ModelViewSet

class ShoeViewSet(ModelViewSet):
    serializer_class = ShoeSerializer
    basename = 'shoe'
    queryset = Shoe.objects.all()


class ShoeTypeViewSet(ModelViewSet):
    serializer_class = ShoeTypeSerializer
    basename = 'shoetype'
    queryset = ShoeType.objects.all()

class ShoeColorViewSet(ModelViewSet):
    serializer_class = ShoeColorSerializer
    basename = 'shoecolor'
    queryset = ShoeColor.objects.all()

class ManufacturerViewSet(ModelViewSet):
    serializer_class = ManufacturerSerializer
    basename = 'manufacturer'
    queryset = Manufacturer.objects.all()