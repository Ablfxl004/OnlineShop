from django.urls import path
from . import views

urlpatterns = [
    path('', views.HoemPageView.as_view(), name='home'),
    path('aboutus', views.AboutUsPageView.as_view(), name='about_us'),
    path('contactus', views.ContactUsPageView.as_view(), name='contact_us'),
]