from django.urls import path

from catalog.apps import CatalogConfig

from . import views

app_name = CatalogConfig.name


urlpatterns = [
    path('base/', views.base, name='base'),
    path('contacts/', views.contacts, name='contacts'),
    path('contact_answer/', views.contact_answer, name='contact_answer'),
    path('product_detail/<int:pk>', views.product_detail, name='product_detail'),
    path('test_base/', views.test_base, name='test_base'),
    path('', views.home, name='home'),
    path('orders/', views.orders, name='orders'),
    path('127.0.0.1:8000', views.catalog_view, name='catalog'),
]
