from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from users.models import CustomUser


class Category(models.Model):
    """Категория услуги или проекта."""

    title = models.CharField(
        verbose_name="название",
        max_length=70,
    )
    parent = models.ForeignKey(
        verbose_name="родительская категория",
        to="Category",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="subcategories",
    )

    class Meta:
        ordering = ["title"]
        verbose_name = "категория"
        verbose_name_plural = "категории"

    def __str__(self):
        title = self.title
        parent = self.parent
        while parent:
            title = f"{parent.title} / {title}"
            parent = parent.parent
        return title


class Chat(models.Model):
    """Чат объединяет сообщения и topic – модель БД, с которой связан чат (заказ, проект...)"""

    topic_ct = models.ForeignKey(
        ContentType,
        blank=True,
        null=True,
        related_name="topic_obj",
        on_delete=models.CASCADE,
    )
    topic_id = models.PositiveIntegerField(
        null=True,
        blank=True,
    )
    topic = GenericForeignKey(
        ct_field="topic_ct",
        fk_field="topic_id",
    )
    latest_message = models.OneToOneField(
        to="Message",
        verbose_name="Последнее сообщение",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="latest_in_chat",
    )
    created = models.DateTimeField(
        verbose_name="создан",
        auto_now_add=True,
    )
    updated = models.DateTimeField(
        verbose_name="изменен",
        auto_now=True,
    )

    class Meta:
        ordering = ["-created"]
        verbose_name = "чат"
        verbose_name_plural = "чаты"

    def __str__(self):
        return f"Чат {self.pk}"


class Message(models.Model):
    """Сообщение в чате."""

    chat = models.ForeignKey(
        to=Chat,
        verbose_name="чат",
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        related_name="messages",
    )
    sender = models.ForeignKey(
        to=CustomUser,
        verbose_name="отправитель",
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        related_name="messages_sent",
    )
    recipient = models.ForeignKey(
        to=CustomUser,
        verbose_name="получатель",
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        related_name="messages_received",
    )
    text = models.TextField(
        verbose_name="Текст сообщения",
        max_length=1500,
        blank=False,
        null=False,
    )
    file = models.FileField(
        verbose_name="вложение",
        help_text="Файл, прилагаемый к сообщению.",
        upload_to="attachments/",
        blank=True,
        null=True,
    )
    is_read = models.BooleanField(
        verbose_name="прочитано",
        help_text="Сообщение прочитано получателем.",
        default=False,
    )
    created = models.DateTimeField(
        verbose_name="создано",
        auto_now_add=True,
    )
    updated = models.DateTimeField(
        verbose_name="изменено",
        auto_now=True,
    )

    class Meta:
        ordering = ["-created"]
        verbose_name = "cообщение"
        verbose_name_plural = "сообщения"

    def __str__(self):
        return (
            f"Сообщение {self.pk} от {self.sender.username} к {self.recipient.username}"
        )
