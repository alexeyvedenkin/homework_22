from django.urls import path
from blog.apps import BlogConfig
from blog.views import (
    ArticleListView,
    ArticleDetailView,
    ArticleCreateView,
    ArticleUpdateView,
    ArticleDeleteView,
    ContactsTemplateView,
    HomeTemplateView,
)

app_name = BlogConfig.name

urlpatterns = [
    path("product_list/", ArticleListView.as_view(), name="product_list"),
    path(
        "product_detail/<int:pk>/", ArticleDetailView.as_view(), name="product_detail"
    ),
    path("product_create/", ArticleCreateView.as_view(), name="product_create"),
    path(
        "product/<int:pk>/update/", ArticleUpdateView.as_view(), name="product_update"
    ),
    path(
        "product/<int:pk>/delete/", ArticleDeleteView.as_view(), name="product_delete"
    ),
    path("", HomeTemplateView.as_view(), name="home"),
    path("contacts/", ContactsTemplateView.as_view(), name="contacts"),
]
