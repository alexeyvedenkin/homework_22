from django.urls import path
from blog.apps import BlogConfig
from blog.views import (
    ArticleListView,
    ArticleDetailView,
    ArticleCreateView,
    ArticleUpdateView,
    ArticleDeleteView,
    HomeTemplateView, UserOwnedArticleListView, publish_article, unpublish_article, NonPublishedArticleListView,
)

app_name = BlogConfig.name

urlpatterns = [
    path("blog/article_list/", ArticleListView.as_view(), name="article_list"),
    path("blog/article_create/", ArticleCreateView.as_view(), name="article_create"),
    path("blog/article_detail/<int:pk>/", ArticleDetailView.as_view(), name="article_detail"),
    path("blog/article/update/<int:pk>/", ArticleUpdateView.as_view(), name="article_form"),
    path("blog/article/<int:pk>/delete/", ArticleDeleteView.as_view(), name="article_delete"),
    path("", HomeTemplateView.as_view(), name="home"),
    path("non_published_articles/", NonPublishedArticleListView.as_view(), name="non_published_articles"),
    path('owned-articles/', UserOwnedArticleListView.as_view(), name='user_owned_articles'),
    path('article/<int:article_id>/publish/', publish_article, name='publish_article'),
    path('article/<int:article_id>/unpublish/', unpublish_article, name='unpublish_article'),

]
