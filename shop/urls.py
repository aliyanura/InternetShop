from django.urls import path
from shop.views import *

urlpatterns = [
    path('home/', home, name='home'),
    path('category/<int:pk>/', product_list, name='product_list'),
    path('category/<int:pk>/product/<int:product_pk>/', product_detail, name='product_detail'),
]