from django.db import models
from PIL import Image

class Product(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=50.99)
    image = models.ImageField(upload_to='', default='apple.jpg', blank=True)


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.image:
            img = Image.open(self.image.path)

            if img.height > 100 or img.width > 100:
                output_size = (100, 100)
                img.thumbnail(output_size)
                img.save(self.image.path)

    def __str__(self):
        return self.title
    
    @property
    def sale_price(self):
        return "%.2f" %(float(self.price) * 0.8)
    
    def get_discount(self):
        return '124'