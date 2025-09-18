from django.shortcuts import render, redirect, get_object_or_404
from .models import Phone


def index(request):
    return redirect('catalog')

def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort')  # получаем параметр сортировки
    phones = Phone.objects.all()
    if sort == 'name':
        phones = phones.order_by('name')
    elif sort == 'min_price':
        phones = phones.order_by('price')
    elif sort == 'max_price':
        phones = phones.order_by('-price')
    context = {
        'phones': phones
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = get_object_or_404(Phone, slug=slug)
    context = {
        'phone': phone
    }
    return render(request, template, context)
