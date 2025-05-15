from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'catalog/home.html')


def contact(request):
    return render(request, 'catalog/contacts.html')


def contact_answer(request):
    if request.method == 'POST':
        # Получение данных из формы
        name = request.POST.get('name')
        message = request.POST.get('message')
        # Обработка данных (например, сохранение в БД, отправка email и т. д.)
        # Здесь мы просто возвращаем простой ответ
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")
    return render(request, 'catalog/contact.html')
