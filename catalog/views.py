from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from catalog.models import Product, Category


def base(request):
    """ Выполняет переход к странице catalog/base.html """
    return render(request, 'catalog/base.html')


def contacts(request):
    """ Выполняет переход к странице catalog/contacts.html """
    return render(request, 'catalog/contacts.html')


def contact_answer(request):
    """ Выполняет запрос сообщения от пользователя.
        Возвращает уведомление о получении данных """
    if request.method == 'POST':
        name = request.POST.get('name')
        message = request.POST.get('message')
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")
    return render(request, 'catalog/contacts.html')


def product_detail(request,pk):
    """ Возвращает детальную информацию о товаре """
    product = get_object_or_404(Product, pk=pk)
    context= {'product': product}
    return render(request, 'catalog/product_detail.html', context)


def test_base(request):
    """ Выполняет переход к странице catalog/test_base.html """
    return render(request, 'catalog/test_base.html')


def index(request):
    """ Выполняет переход к странице catalog/test_base.html """
    return render(request, 'catalog/index.html')


def orders(request):
    """ Выполняет переход к странице catalog/test_base.html """
    return render(request, 'catalog/orders.html')


def catalog(request):
    """ Выполняет переход к странице catalog/test_base.html """
    return render(request, 'catalog/catalog.html')


def home(request):
    products = Product.objects.all()  # Извлечение всех продуктов
    return render(request, 'catalog/home.html', {'products': products})


def catalog_view(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})
