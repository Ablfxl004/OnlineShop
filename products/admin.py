from django.contrib import admin
from .models import Product, ProductComment
# Register your models here.


class CommentsInline(admin.StackedInline):
    model = ProductComment
    fields = ('author', 'body', 'active',)
    extra = 0

@admin.register(Product)
class ProcustAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'datetime_modified', 'active')
    inlines = (
        CommentsInline,
    )

@admin.register(ProductComment)
class ProcustCommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'body', 'datetime', 'active', 'product')