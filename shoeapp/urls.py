from django.urls import path
from shoeapp import views

urlpatterns = [
    path('', views.index, name = 'homepage'),
    path('shoeadd/', views.AddShoe.as_view(), name="shoe_add_view"),
    path('manufactureradd/', views.AddManufacturer.as_view(), name="manufacturer_add_view"),
    path('shoe/<int:id>/', views.ShoeDetails.as_view(), name="shoe_details"),
    path('manufacturer/<int:id>/', views.ManufacturerDetails.as_view(), name="manufacturer_details"),
]

