from django.contrib import admin

from blog.models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "content", "active_is", "views_counter")
    list_filter = ("active_is",)
    search_fields = ("title", "active_is")
