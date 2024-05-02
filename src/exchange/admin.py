from django.contrib import admin

from exchange.models import Category, Chat, Message


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


@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    model = Chat
    list_display = [
        "id",
        "created",
        "topic",
    ]
    ordering = [
        "-created",
    ]


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    model = Message
    list_display = [
        "id",
        "chat",
        "sender",
        "recipient",
        "is_read",
        "created",
    ]
    ordering = [
        "-created",
    ]
