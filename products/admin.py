from django.contrib import admin
from .models import Product, ProductComment
from jalali_date.admin import ModelAdminJalaliMixin


class CommentsInline(admin.StackedInline):
    model = ProductComment
    fields = ('author', 'body', 'active',)
    extra = 0

@admin.register(Product)
class ProcustAdmin(ModelAdminJalaliMixin,admin.ModelAdmin):
    list_display = ('title', 'price', 'datetime_modified', 'active')
    inlines = (
        CommentsInline,
    )

@admin.register(ProductComment)
class ProcustCommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'body', 'datetime', 'active', 'product')