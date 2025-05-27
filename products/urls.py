from django.urls import path

from .views import ProductListView, ProductDetailView,CommentCreateView, test_messages


urlpatterns = [
    path('', ProductListView.as_view(), name='products_list'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('comment/<int:pk>', CommentCreateView.as_view(), name='comment_create'),
    path('messages/', test_messages, name='test_messages'),
]