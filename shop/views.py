from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.db.models import Count


def home(request):
    categories = Category.objects.all()
    return render(request, 'home.html', locals())

def product_list(request, pk):
    category = get_object_or_404(Category, pk=pk)
    products = category.products.all()
    return render(request, 'products_list.html', locals())

def product_detail(request, pk, product_pk):
    product = get_object_or_404(Product, category__pk=pk, pk=product_pk)
    prodname = ' '.join(product.name.split()[:3])
    print(prodname)
    return render(request, 'product_detail.html', locals())