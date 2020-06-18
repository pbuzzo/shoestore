from shoeapp.models import Shoe, Manufacturer
from django import forms


class ManufacturerAddForm(forms.ModelForm):
    class Meta:
        model = Manufacturer
        fields = ('name', 'website')


class ShoeAddForm(forms.ModelForm):
    class Meta:
        model = Shoe
        fields = (
            'size',
            'brand_name',
            'manufacturer',
            'color',
            'material',
            'shoe_type',
            'fasten_type'
        )
