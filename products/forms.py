from .models import ProductComment
from django import forms


class ProductCommentForm(forms.ModelForm):
    class Meta:
        model = ProductComment
        fields = ('body', 'starts')