from django.urls import path

from . import views

app_name = 'catalog'


urlpatterns = [
    path('home/', views.home, name='home'),
    path('contacts/', views.contacts, name='contacts'),
    path('contact_answer/', views.contact_answer, name='contact_answer'),
]
