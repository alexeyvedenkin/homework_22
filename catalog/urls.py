from django.urls import path
from . import views


app_name = 'catalog'


urlpatterns = [
    path('home/', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('contact_answer/', views.contact_answer, name='contact_answer'),
]
