from django.core.cache import cache
from django.db import models

from catalog.models import Product, Category
from config.settings import CACHE_ENABLED


class CategoryDetail(models.Model):

    @staticmethod
    def get_products_from_cache():
        """ Получает данные о товарах из кэша.
        Если в кэше нет данных, получает их из БД и записывает в кэш """
        if not CACHE_ENABLED:
            return Product.objects.all()
        key = 'products_list'
        products = cache.get(key)
        if products is not None:
            return products
        products = Product.objects.all()
        cache.set(key, products)
        return products


    @staticmethod
    def get_products_list_from_category(category_id):
        """ Получает данные о товарах в категории из кэша.
        Если в кэше нет данных, получает их из БД и записывает в кэш """

        if not CACHE_ENABLED:
            return Product.objects.filter(category_id=category_id)

        key = f'products_list_{category_id}'
        products = cache.get(key)

        if products is not None:
            return products
        products = Product.objects.filter(category_id=category_id)
        cache.set(key, products)
        return products
