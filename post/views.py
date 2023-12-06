from django.shortcuts import HttpResponse, render
from datetime import date

from post.models import Product, Category


def main_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')


def products_view(request):
    if request.method == 'GET':
        products = Product.objects.all()

        return render(request, 'products/products.html', context={"products": products})


def category_view(request):
    if request.method == 'GET':
        category = Category.objects.all()
        return render(request, 'products/category.html', {"category": category})


def product_detail_view(request, prod_id):
    if request.method == 'GET':
        product = Product.objects.get(id=prod_id)
        return render(request, 'products/detail.html', {'product': product})
