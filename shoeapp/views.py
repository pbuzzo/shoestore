from django.shortcuts import render, reverse, HttpResponseRedirect
from shoeapp.models import Shoe, Manufacturer
from shoeapp.forms import ShoeAddForm, ManufacturerAddForm
from django.views.generic import View


def index(request):
    shoes = Shoe.objects.all()
    manufacturers = Manufacturer.objects.all()
    return render(request, 'index.html', {shoes: 'shoes', manufacturers: 'manufacturers'})

class AddShoe(View):
    def get(self, request):
        html = 'shoe_form.html'
        form = ShoeAddForm()
        return render(request, html, {'form': form})
    def post(self, request):
        form = ShoeAddForm(request.POST)
        shoes = Shoe.objects.all()
        if form.is_valid():
            data = form.cleaned_data
            Shoe.objects.create(
                name=data['name'],
                size=data['size'],
                brand_name=data['brand_name'],
                manufacturer=data['manufacturer'],
                color=data['color'],
                material=data['material'],
                shoe_type=data['shoe_type'],
                fasten_type=data['fasten_type'],
            )
        return HttpResponseRedirect(reverse("homepage"))

class AddManufacturer(View):
    def get(self, request):
        html = 'manufacturer_form.html'
        form = ManufacturerAddForm()
        return render(request, html, {'form': form})
    def post(self, request):
        form = ManufacturerAddForm(request.POST)
        manufacturers = Manufacturer.objects.all()
        if form.is_valid():
            data = form.cleaned_data
            Manufacturer.objects.create(
                name=data['name'],
                website=data['website'],
            )
        return HttpResponseRedirect(reverse("homepage"))


class ShoeDetails(View):
    def get(self, request, id):
        shoe = Shoe.objects.get(id=id)
        return render(request, "shoe_details.html", {"shoe": shoe})


class ManufacturerDetails(View):
    def get(self, request, id):
        manufacturer = Manufacturer.objects.get(id=id)
        return render(request, "manufacturer_details.html", {"manufacturer": manufacturer})