from django.contrib import admin
from .models import Product
# Register your models here.

@admin.register(Product)
class ProcustAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'datetime_modified', 'active')

