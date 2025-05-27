from django.shortcuts import render, get_object_or_404, HttpResponse
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse
from django.contrib import messages
from django.utils.translation import gettext_lazy as _



from .models import Product, ProductComment
from .forms import ProductCommentForm
from cart.forms import AddToCartProductForm


def test_messages(request):
    messages.success(request, 'This is a success message')
    messages.error(request, 'this is a error message')
    messages.info(request, 'this is a info message')

    return render(request, 'products/messages.html')


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
        context['add_to_cart_form'] = AddToCartProductForm()

        return context
    
class CommentCreateView(CreateView):
    model = ProductComment
    form_class = ProductCommentForm

    def form_valid(self, form):
        if not self.request.user.is_authenticated:
            return HttpResponse("You must be logged in to post a comment.")
        obj = form.save(commit=False)
        obj.author = self.request.user
        pro_id = int(self.kwargs['pk'])
        obj.product = get_object_or_404(Product, id=pro_id)

        messages.success(self.request, _('Comment successfully created.'))

        return super().form_valid(form)