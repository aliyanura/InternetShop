from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
    def get_products_count(self):
        return Product.objects.filter(category=self).count()

    class Meta:
        verbose_name_plural = 'Categories'

    
class Product(models.Model):
    name = models.CharField(max_length=150)
    price = models.IntegerField(null=True)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    image = models.ImageField(upload_to='products')

    def __str__(self):
        return self.description