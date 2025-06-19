from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import (
    ProductListView,
    ProductDetailView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
    ContactsTemplateView,
    HomeTemplateView,
    NonPublishedProductListView,
    UserOwnedProductListView, publish_product, unpublish_product
)

app_name = CatalogConfig.name

urlpatterns = [
    path("product_list/", ProductListView.as_view(), name="product_list"),
    path("product_detail/<int:pk>/", cache_page(60 * 15)(ProductDetailView.as_view()), name="product_detail"),
    path("product_create/", ProductCreateView.as_view(), name="product_create"),
    path("product/<int:pk>/update/", ProductUpdateView.as_view(), name="product_update"),
    path("product/<int:pk>/delete/", ProductDeleteView.as_view(), name="product_delete"),
    path("", HomeTemplateView.as_view(), name="home"),
    path("contacts/", ContactsTemplateView.as_view(), name="contacts"),
    path("non_published_products/", NonPublishedProductListView.as_view(), name="non_published_products"),
    path('owned-products/', UserOwnedProductListView.as_view(), name='user_owned_products'),
    path('product/<int:product_id>/publish/', publish_product, name='publish_product'),
    path('product/<int:product_id>/unpublish/', unpublish_product, name='unpublish_product'),
]
