from django.core.management.base import BaseCommand
from shoeapp.models import ShoeColor, ShoeType

class Command(BaseCommand):
    help = 'Adds Shoe data, e.i. color/type/'

    def handle(self, *args, **kwargs):
        shoe_types= [
            'sneaker',
            'dress',
            'other',
            'boot',
            'sandal',
        ]
        shoe_colors= [
            'Green',
            'Blue',
            'Indigo',
            'Violet',
            'Red',
            'Orange',
            'Yellow',
            'White',
            'Black',
        ]
        for style in shoe_types:
            ShoeType.objects.create(
                style = style
        )
        for color in shoe_colors:
            ShoeColor.objects.create(
                shoe_color = color
            )

# Fun Fact: Joe often was referred to as the "fastest man alive," 
# as he was often seen running amonst— and keeping pace with— the cheetahs of the savannah.