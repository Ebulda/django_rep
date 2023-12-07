from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from post.forms import ProductCreateForm, CategoryCreateForm, ReviewCreateForm
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


def product_create(request):
    if request.method == 'GET':
        return render(request, 'products/create_prod.html', {'form': ProductCreateForm})
    if request.method == "POST":
        form = ProductCreateForm(request.POST, request.FILES)
        if form.is_valid():
            Product.objects.create(**form.cleaned_data)
            return redirect('/products/')

    return render(request, 'products/create_prod.html', {'form': ProductCreateForm(request.POST, request.FILES)})


def category_create(request):
    if request.method == 'POST':
        form = CategoryCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/category')

    else:
        form = CategoryCreateForm()

    context = {'form': form}
    return render(request, 'products/create_category.html', context)


def review_create(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        form = ReviewCreateForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.save()
            return redirect('/products')

    else:
        form = ReviewCreateForm()

    context = {'form': form, 'product': product}
    return render(request, 'products/create_review.html', context)
