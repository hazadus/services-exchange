from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from users.models import CustomUser


class Order(models.Model):
    """Заказ услуги или проекта."""

    STATUS_CHOICES = (
        ("created", "Размещен заказчиком"),
        ("in_progress", "В работу у исполнителя"),
        ("cancelled_by_customer", "Отменен заказчиком"),
        ("cancelled_by_provider", "Отменен исполнителем"),
        ("submitted_by_provider", "Сдан исполнителем"),
        ("returned_by_customer", "Возвращен заказчиком на доработку"),
        ("accepted_by_customer", "Принят заказчиком"),
        ("paid", "Оплачен"),
        ("completed", "Завершен"),
    )

    customer = models.ForeignKey(
        CustomUser,
        verbose_name="заказчик",
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        related_name="orders_as_customer",
    )
    provider = models.ForeignKey(
        CustomUser,
        verbose_name="исполнитель",
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        related_name="orders_as_provider",
    )
    #
    # item - предмет заказа. Это может быть Project или Service.
    #
    item_ct = models.ForeignKey(
        ContentType,
        blank=False,
        null=False,
        related_name="item_obj",
        on_delete=models.CASCADE,
    )
    item_id = models.PositiveIntegerField(
        null=False,
        blank=False,
    )
    item = GenericForeignKey(
        ct_field="item_ct",
        fk_field="item_id",
    )
    price = models.IntegerField(
        verbose_name="стоимость",
        help_text="Стоимость заказа в руб.",
        null=False,
        blank=False,
    )
    status = models.CharField(
        verbose_name="статус заказа",
        choices=STATUS_CHOICES,
        default="created",
        max_length=32,
    )
    comment = models.TextField(
        verbose_name="комментарий к заказу",
        max_length=1500,
        blank=True,
        null=True,
    )
    is_completed = models.BooleanField(
        verbose_name="завершен",
        default=False,
    )
    is_paid = models.BooleanField(
        verbose_name="оплачен",
        default=False,
    )
    is_cancelled = models.BooleanField(
        verbose_name="отменен",
        default=False,
    )
    created = models.DateTimeField(
        verbose_name="создан",
        auto_now_add=True,
    )
    updated = models.DateTimeField(
        verbose_name="обновлен",
        auto_now=True,
    )

    class Meta:
        ordering = ["-created"]
        verbose_name = "заказ"
        verbose_name_plural = "заказы"

    def __str__(self):
        return f"Заказ №{self.id}"
