from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models


class Product(models.Model):
    name = models.CharField(
        max_length=100, verbose_name="Товар",
    )
    description = models.TextField(
        verbose_name="Описание",
    )
    product_image = models.ImageField(
        upload_to="products/images",
        verbose_name="Изображение",
        blank=True,
        null=True,
    )
    category = models.ForeignKey(
        "Category",
        on_delete=models.SET_NULL,
        max_length=100,
        verbose_name="Категория",
        blank=True,
        null=True,
        related_name="products",
    )
    price = models.FloatField(verbose_name="Цена")
    create_date = models.DateField(
        verbose_name="Дата создания",
        blank=True,
        null=True,
    )
    update_date = models.DateField(
        verbose_name="Дата последнего обновления", blank=True, null=True
    )

    is_published = models.BooleanField(
        default=False,
        verbose_name="Опубликовано"
    )

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Владелец",
    )

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ["owner", "name"]
        permissions = [
            ("can_unpublish_product", "Can unpublish product"),
        ]

    def save(self, *args, **kwargs):
        if not self.owner:
            self.owner = get_user_model().objects.get(id=kwargs.pop('user_id'))
        super().save(*args, **kwargs)


    def __str__(self):
        return f"Наименование: {self.name}, цена: {self.price}"


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Категория",
        help_text="Введите наименование категории",
    )
    description = models.TextField(
        verbose_name="Описание", help_text="Введите описание категории"
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]

    def __str__(self):
        return self.name
