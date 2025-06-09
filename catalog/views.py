from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    TemplateView,
    UpdateView,
)

from catalog.models import Product
from catalog.forms import ProductForm

class ProductListView(ListView):
    model = Product
    context_object_name = 'products'

class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy("catalog:product_list")


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy("catalog:product_list")


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:product_list")


class ContactsTemplateView(TemplateView):
    """Выполняет переход к странице catalog/contacts.html"""

    template_name = "catalog/contacts.html"


class HomeTemplateView(TemplateView):
    """Выполняет переход к странице catalog/contacts.html"""

    template_name = "catalog/home.html"
