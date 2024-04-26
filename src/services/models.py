from django.db import models
from exchange.models import Category
from users.models import CustomUser


class Service(models.Model):
    """Услуга, предлагаемая пользователем сайта."""

    provider = models.ForeignKey(
        verbose_name="исполнитель услуги",
        help_text="Пользователь, который предоставляет данную услугу",
        to=CustomUser,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name="services",
    )
    title = models.CharField(
        verbose_name="название",
        max_length=70,
        null=False,
        blank=False,
    )
    category = models.ForeignKey(
        verbose_name="рубрика",
        help_text="Категория, в которой будет размещена услуга",
        to=Category,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name="services",
    )
    image = models.ImageField(
        verbose_name="обложка",
        null=True,
        blank=True,
        upload_to="images/services/",
    )
    description = models.TextField(
        verbose_name="описание",
        help_text="Подробное описание предрставляемой услуги",
        max_length=1200,
        null=False,
        blank=False,
    )
    requirements = models.TextField(
        verbose_name="от покупателя нужно",
        help_text="Укажите что требуется от заказчика услуги. Например, ТЗ, доступы, и т.п.",
        max_length=500,
        null=False,
        blank=False,
    )
    price = models.IntegerField(
        verbose_name="стоимость",
        help_text="Стоимость услуги в руб.",
        null=False,
        blank=False,
    )
    term = models.IntegerField(
        verbose_name="срок",
        help_text="Срок выполнения услуги, в днях",
        null=False,
        blank=False,
    )
    options = models.TextField(
        verbose_name="дополнительные услуги",
        help_text="Если вы предлагаете дополнительные услуги, расскажите о них. Укажите название, срок, стоимость.",
        max_length=1200,
        null=True,
        blank=True,
    )
    portfolio_url = models.URLField(
        verbose_name="ссылка на портфолио",
        null=True,
        blank=True,
    )
    is_active = models.BooleanField(
        verbose_name="услуга активна",
        help_text="Снимите галочку, чтобы исключить услугу из каталога, не удаляя её.",
        default=True,
    )
    created = models.DateTimeField(
        verbose_name="создана",
        auto_now_add=True,
    )
    updated = models.DateTimeField(
        verbose_name="изменена",
        auto_now=True,
    )

    class Meta:
        ordering = ["-created"]
        verbose_name = "услуга"
        verbose_name_plural = "услуги"

    def __str__(self):
        return self.title
