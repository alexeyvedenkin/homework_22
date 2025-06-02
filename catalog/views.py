from django.http import HttpResponse
from django.shortcuts import render

from catalog.models import Product


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


def product_detail(request):
    """ Возвращает детальную информацию о товаре """
    product = Product.object.get(pk=pk)
    context= {'product': product}
    return render(request, 'product_detail.html', context)
