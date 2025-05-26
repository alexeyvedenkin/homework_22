from django.db import models


class Product(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Товар',
        help_text='Введите наименование товара'
    )
    description = models.TextField(
        verbose_name='Описание',
        help_text='Введите описание товара'
    )
    product_image = models.ImageField(
        upload_to='products/images',
        verbose_name='Изображение',
        help_text='Загрузите изображение товара',
        blank=True,
        null=True
    )
    category = models.ForeignKey(
        'Category',
        on_delete=models.SET_NULL,
        max_length=100,
        verbose_name='Категория',
        help_text='Введите категорию товара',
        blank=True,
        null=True,
        related_name='products',
    )
    price = models.FloatField(
        verbose_name='Цена',
        help_text='Введите цену товара'
    )
    create_date = models.DateField(
        verbose_name='Дата создания',
        help_text='Введите дату создания товара',
        blank=True,
        null=True
    )
    update_date = models.DateField(
        verbose_name='Дата последнего обновления',
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['category', 'name']

    def __str__(self):
        return f'Наименование: {self.name}, цена: {self.price}'


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Категория',
        help_text='Введите наименование категории'
    )
    description = models.TextField(
        verbose_name='Описание',
        help_text='Введите описание категории'
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']

    def __str__(self):
        return self.name
