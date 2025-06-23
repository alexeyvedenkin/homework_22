from django.contrib.auth.decorators import permission_required, login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    TemplateView,
    UpdateView,
)

from catalog.models import Product, Category
from catalog.forms import ProductForm, CategoryForm
from catalog.services import CategoryDetail


class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'product_list.html'

    def get_queryset(self):
        return Product.objects.filter(is_published=True)

    @staticmethod
    def get_full_queryset():
        return CategoryDetail.get_products_from_cache()

class NonPublishedProductListView(ListView):
    model = Product
    context_object_name = 'non_published_products'
    template_name = 'catalog/non_published_products.html'

    def get_queryset(self):
        return Product.objects.filter(is_published=False)


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy("catalog:product_list")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy("catalog:product_list")


class UserOwnedProductListView(LoginRequiredMixin, ListView):
    model = Product
    context_object_name = 'owned_products'
    template_name = 'catalog/user_author_products.html'

    def get_queryset(self):
        return Product.objects.filter(owner=self.request.user)


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:product_list")


@login_required
@permission_required('catalog.can_unpublish_product', raise_exception=True)
def publish_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    product.is_published = True
    product.save()
    return redirect('catalog:non_published_products')


@login_required
@permission_required('catalog.can_unpublish_product', raise_exception=True)
def unpublish_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    product.is_published = False
    product.save()
    return redirect('catalog:non_published_products')


class ContactsTemplateView(TemplateView):
    """Выполняет переход к странице catalog/contacts.html"""

    template_name = "catalog/contacts.html"


class HomeTemplateView(TemplateView):
    """Выполняет переход к странице catalog/contacts.html"""

    template_name = "catalog/home.html"


class CategoryListView(ListView):
    model = Category
    template_name = 'catalog/category_list.html'
    context_object_name = 'categories'


class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'catalog/category_form.html'
    success_url = reverse_lazy("catalog:category_list")


class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'catalog/category_form.html'
    success_url = reverse_lazy("catalog:category_list")



class CategoryDeleteView(DeleteView):
    model = Category
    success_url = reverse_lazy("catalog:category_list")


class CategoryDetailView(DetailView):
    """Отображает детали выбранной категории, включая продукты"""
    model = Category
    template_name = 'catalog/category_detail.html'  # Specify your template name
    context_object_name = 'category'  # Context variable name for the category

    def get_context_data(self, **kwargs):
        """Add products to the context based on the category"""
        context = super().get_context_data(**kwargs)

        context['products'] = CategoryDetail.get_products_list_from_category(self.object.id)
        return context
