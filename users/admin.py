from django.contrib import admin

from users.models import CustomUser


@admin.register(CustomUser)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "email", "username", "phone_number", "country")
    list_filter = ("country",)
    search_fields = ("username",)
