from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator


def store(request):
    # products = Product.objects.order_by('name')
    p = Paginator(Product.objects.order_by('name'), 1)
    page = request.GET.get('page')
    products = p.get_page(page)
    # img = products.productimage_set.first.image()
    # page_count = products.paginator.num_pages
    dummy = "a" * products.paginator.num_pages
    context = {'products': products,
               'dummy': dummy}
    return render(request, 'store/store.html', context)


def cart(request):
    context = {}
    return render(request, 'store/cart.html', context)


def detail(request):
    context = {}
    return render(request, 'store/detail.html', context)


def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)


def login(request):
    context = {}
    return render(request, 'user/login.html', context)


def register(request):
    context = {}
    return render(request, 'user/register.html', context)


def logout(request):
    context = {}
    return render(request, 'user/logout.html', context)
