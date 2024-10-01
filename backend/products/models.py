from django.db import models
from PIL import Image
from django.conf import settings
from django.db.models import Q
import random

User = settings.AUTH_USER_MODEL # auth.User

TAGS_MODEL_VALUES = ['car', 'book', 'pen', 'electronics', 'mobile']

class ProductQuerySet(models.QuerySet):
    def is_public(self):
        return self.filter(public=True)

    def search(self, query, user=None):
        lookup = Q(title__icontains=query) | Q(content__icontains=query)
        qs = self.is_public().filter(lookup)
        if user is not None:
            qs2 = self.filter(user=user).filter(lookup)
            qs = (qs|qs2).distinct()
        return qs
    
class ProductManager(models.Manager):
    def get_queryset(self, *args, **kwarg):
        return ProductQuerySet(self.model, using=self._db)
    
    
class Product(models.Model):
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=50)
    content = models.CharField(default='I love fruits')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=150.99)
    image = models.ImageField(upload_to='', default='apple.jpg')
    public = models.BooleanField(default=True)

    objects = ProductManager()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.image:
            img = Image.open(self.image.path)

            if img.height > 100 or img.width > 100:
                output_size = (100, 100)
                img.thumbnail(output_size)
                img.save(self.image.path)

    def get_discount(self):
        return '124'
    
    def __str__(self):
        return self.title
    
    @property
    def sale_price(self):
        return "%.2f" %(float(self.price) * 0.8)
    
    # method for algolia search
    def is_public(self):
        return self.public
    
    def get_tags_list(self):
        return [random.choice(TAGS_MODEL_VALUES)]
    
    
   