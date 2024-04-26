from django.contrib import admin

from exchange.models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = [
        "title",
        "parent",
    ]
    ordering = [
        "id",
        "parent",
    ]
