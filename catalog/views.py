from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    """ Выполняет переход к странице catalog/home.html """
    return render(request, 'catalog/home.html')


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
