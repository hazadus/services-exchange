from django.db import models
from exchange.models import Category
from users.models import CustomUser


class Project(models.Model):
    """Проект, предлагаемый пользователем для реализации другими пользователями."""

    customer = models.ForeignKey(
        verbose_name="заказчик проекта",
        help_text="Пользователь, который предлагает данный проект для реализации",
        to=CustomUser,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name="projects",
    )
    title = models.CharField(
        verbose_name="название",
        max_length=70,
        null=False,
        blank=False,
    )
    category = models.ForeignKey(
        verbose_name="рубрика",
        help_text="Категория, в которой будет размещен проект",
        to=Category,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name="projects",
    )
    description = models.TextField(
        verbose_name="детальное описание задачи",
        help_text="Опишите, что именно вам нужно, в каком объеме и за какой срок.",
        max_length=5200,
        null=False,
        blank=False,
    )
    price = models.IntegerField(
        verbose_name="цена не более",
        help_text="Ваш бюджет в руб.",
        null=False,
        blank=False,
    )
    is_higher_price_allowed = models.BooleanField(
        verbose_name="Готов рассмотреть предложения с ценой выше, если уровень исполнителя будет выше",
        default=False,
    )
    max_price = models.IntegerField(
        verbose_name="максимальная цена",
        help_text="Максимальная цена в случае высокого уровня исполнителя.",
        null=True,
        blank=True,
    )
    is_active = models.BooleanField(
        verbose_name="проект активен",
        help_text="Снимите галочку, чтобы исключить проект из каталога, не удаляя его.",
        default=True,
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
        verbose_name = "проект"
        verbose_name_plural = "проекты"

    def __str__(self):
        return self.title
