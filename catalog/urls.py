from django.urls import path

# from catalog.apps import CatalogConfig

from . import views

app_name = 'catalog'


urlpatterns = [
    path('base/', views.base, name='base'),
    path('contacts/', views.contacts, name='contacts'),
    path('contact_answer/', views.contact_answer, name='contact_answer'),
    path('product_detail/<int: pk>', views.product_detail, name='product_detail')
]
