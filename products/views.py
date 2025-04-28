from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse


from .models import Product, ProductComment
from .forms import ProductCommentForm

class ProductListView(ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'
    queryset = Product.objects.filter(active=True)

class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = ProductCommentForm()

        return context
    
class CommentCreateView(CreateView):
    model = ProductComment
    form_class = ProductCommentForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        pro_id = int(self.kwargs['pk'])
        obj.product = get_object_or_404(Product, id=pro_id)

        return super().form_valid(form)