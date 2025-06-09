from django.db import models


class Article(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name="Статья",
    )
    content = models.TextField(
        verbose_name="Содержание",
    )
    preview = models.ImageField(
        upload_to="article/images",
        verbose_name="Изображение",
        blank=True,
        null=True,
    )
    create_at = models.DateTimeField(
        auto_now_add=True,
    )
    active_is = models.BooleanField(
        verbose_name="Признак публикации",
    )
    views_counter = models.PositiveIntegerField(
        verbose_name="Количество просмотров", default=0
    )

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
        ordering = ["views_counter"]

    def __str__(self):
        return self.title
