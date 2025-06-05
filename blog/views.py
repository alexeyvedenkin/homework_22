from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    TemplateView,
    UpdateView,
)

from blog.models import Article


class ArticleListView(ListView):
    model = Article


class ArticleDetailView(DetailView):
    model = Article


class ArticleCreateView(CreateView):
    model = Article
    fields = ("title", "content", "views_counter", "create_at", "preview", "active_is")
    success_url = reverse_lazy("blog:article_list")


class ArticleUpdateView(UpdateView):
    model = Article
    fields = ("title", "content", "views_counter", "create_at", "preview", "active_is")
    success_url = reverse_lazy("blog:article_list")


class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy("blog:article_list")


class ContactsTemplateView(TemplateView):
    """Выполняет переход к странице catalog/contacts.html"""

    template_name = "catalog/contacts.html"


class HomeTemplateView(TemplateView):
    """Выполняет переход к странице catalog/contacts.html"""

    template_name = "catalog/home.html"

