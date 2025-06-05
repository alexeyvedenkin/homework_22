from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, TemplateView, UpdateView

from catalog.models import Product


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    fields = ('name', 'description', 'price', 'create_date', 'product_image')
    success_url = reverse_lazy('catalog:product_list')


class ProductUpdateView(UpdateView):
    model = Product
    fields = ('name', 'description', 'price', 'create_date', 'product_image')
    success_url = reverse_lazy('catalog:product_list')


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')


class ContactsTemplateView(TemplateView):
    """ Выполняет переход к странице catalog/contacts.html """
    template_name = 'catalog/contacts.html'


class HomeTemplateView(TemplateView):
    """ Выполняет переход к странице catalog/contacts.html """
    template_name = 'catalog/home.html'
