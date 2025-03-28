from django.db import models
from django.urls import reverse

class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    # cover = models.ImageField()

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("product_detail", args={self.id, })