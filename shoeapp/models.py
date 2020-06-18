from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=50)
    website = models.URLField(max_length = 200)


class ShoeType(models.Model):
    style = models.CharField(max_length=30)

    def __str__(self):
        return self.style


class ShoeColor(models.Model):
    color_list = [
        ('red', 'red'),
        ('orange', 'orange'),
        ('yellow', 'yellow'),
        ('green', 'green'),
        ('blue', 'blue'),
        ('indigo', 'indigo'),
        ('violet', 'violet'),
        ('white', 'white'),
        ('black', 'black')
    ]
    color_name = models.CharField(
        max_length=6,
        choices=color_list,
        default='white'
    )

    def __str__(self):
        return self.color_name


class Shoe(models.Model):
    size = models.IntegerField()
    brand_name = models.CharField(max_length=30)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    color = models.ForeignKey(ShoeColor, on_delete=models.CASCADE)
    material = models.CharField(max_length=30)
    shoe_type = models.ForeignKey(ShoeType, on_delete=models.CASCADE)
    fasten_type = models.CharField(max_length=30)