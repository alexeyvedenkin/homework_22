import os

from dotenv import load_dotenv
from django.core.mail import send_mail
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import (
    DeleteView,
    DetailView,
    ListView,
    TemplateView,
)

from blog.models import Article

load_dotenv(override=True)


class ArticleCreateView(CreateView):
    model = Article
    fields = ("title", "content", "views_counter", "preview", "active_is")
    template_name = 'blog/article_form.html'
    success_url = reverse_lazy("blog:article_list")


class ArticleListView(ListView):
    model = Article
    template_name = 'blog/article_list.html'
    context_object_name = 'articles'

    def get_queryset(self):
        return Article.objects.filter(active_is=True)


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'blog/article_detail.html'
    context_object_name = 'article'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object

        if self.object.views_counter == 100:
            self.send_congratulation_email()

        return self.object

    def send_congratulation_email(self):
        subject = 'Поздравляем!'
        message = f'Ваша статья {self.object.title} набрала 100 просмотров!'
        from_email = os.getenv("FROM_EMAIL")
        recipient_list = [os.getenv("RECIPIENT_EMAIL")]

        send_mail(subject, message, from_email, recipient_list)


class ArticleUpdateView(UpdateView):
    model = Article
    fields = ("title", "content", "views_counter")
    template_name = 'blog/article_form.html'
    success_url = reverse_lazy("blog:article_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_success_url(self):
        return reverse('blog:article_detail', args=[self.kwargs.get('pk')])


class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy("blog:article_list")


class ContactsTemplateView(TemplateView):
    """Выполняет переход к странице catalog/contacts.html"""

    template_name = "catalog/contacts.html"


class HomeTemplateView(TemplateView):
    """Выполняет переход к странице catalog/contacts.html"""

    template_name = "catalog/home.html"
