import os
from django import forms
from .models import Product
from dotenv import load_dotenv
from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import InMemoryUploadedFile
from PIL import Image

FORBIDDEN_WORDS=['казино','криптовалюта','крипта','биржа','дешево','бесплатно','обман','полиция','радар']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "price", "create_date", 'update_date', "product_image", 'category',]

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите наименование товара'
        })

        self.fields['description'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите описание товара'
        })

        self.fields['price'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите цену товара'
        })

        self.fields['create_date'].widget.attrs.update({
            'class': 'form-control'
        })

        self.fields['update_date'].widget.attrs.update({
            'class': 'form-control'
        })

        self.fields['product_image'].widget.attrs.update({
            'class': 'form-control'
        })

        self.fields['category'].widget.attrs.update({
            'class': 'form-control'
        })

    def clean_name(self):
        name = self.cleaned_data.get('name')
        for elem in FORBIDDEN_WORDS:
            if elem in name:
                raise ValidationError("В наименовании продукта не должно быть запрещенных слов")
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description')
        for elem in FORBIDDEN_WORDS:
            if elem in description:
                raise ValidationError("В описании продукта не должно быть запрещенных слов")
        return description

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price <= 0:
            raise ValidationError("Цена должна быть положительным числом")
        return price

    def clean_product_image(self):
        product_image = self.cleaned_data.get('product_image')
        if product_image:
            try:
                img = Image.open(product_image)
                if img.format not in ['JPEG', 'PNG']:
                    raise ValidationError("Формат изображения должен быть JPEG или PNG.")
            except IOError:
                raise ValidationError("Ошибка открытия изображения.")

            if product_image.size > 5 * 1024 * 1024:  # Size limit of 5 MB
                raise ValidationError("Размер изображения не должен превышать 5 МБ.")

        return product_image
