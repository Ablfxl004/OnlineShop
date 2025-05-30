from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from ckeditor.fields import RichTextField

class Product(models.Model):
    title = models.CharField(max_length=200)
    description = RichTextField()
    price = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)
    datetime_created = models.DateTimeField(verbose_name=_('Created time'), default=timezone.now)
    datetime_modified = models.DateTimeField(auto_now=True)
    image = models.ImageField(verbose_name=_('Product Image'), upload_to='product/produc_cover/', blank=True)
    # cover = models.ImageField()

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("product_detail", args={self.id, })
    

class ActiveCommentsManager(models.Manager):
    def get_queryset(self):
        return super(ActiveCommentsManager, self).get_queryset().filter(active=True)


class ProductComment(models.Model):
    PRODUCT_STARS = (
        ('1', 'very bad'),
        ('2', 'bad'),
        ('3', 'normal'),
        ('4', 'good'),
        ('5', 'perfect'),
    )

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comments', verbose_name=_('Comment author'))
    body = models.TextField(verbose_name=_('Comment Text: '))
    datetime = models.DateTimeField(auto_now_add=True)
    starts = models.CharField(max_length=5, choices=PRODUCT_STARS, verbose_name=_('What is your rate?'))
    active = models.BooleanField(default=True)

    #manager
    objects = models.Manager()
    active_comments_manager = ActiveCommentsManager()

    def get_absolute_url(self):
        return reverse('product_detail', args={self.product.id, })

    