from django.urls import path
from blog.apps import BlogConfig
from blog.views import (
    ArticleListView,
    ArticleDetailView,
    ArticleCreateView,
    ArticleUpdateView,
    ArticleDeleteView,
    HomeTemplateView,
)

app_name = BlogConfig.name

urlpatterns = [
    path("blog/article_list/", ArticleListView.as_view(), name="article_list"),
    path("blog/article_create/", ArticleCreateView.as_view(), name="article_create"),
    path("blog/article_detail/<int:pk>/", ArticleDetailView.as_view(), name="article_detail"),
    path("blog/article/update/<int:pk>/", ArticleUpdateView.as_view(), name="article_form"),
    path("blog/article/<int:pk>/delete/", ArticleDeleteView.as_view(), name="article_delete"),
    path("", HomeTemplateView.as_view(), name="home"),

]
