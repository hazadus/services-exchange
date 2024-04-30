from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.postgres.fields import ArrayField
from django.db import models


class CustomUser(AbstractUser):
    """
    Custom user model with additional fields.
    """

    profile_image = models.ImageField(
        verbose_name="изображение профиля",
        null=True,
        blank=True,
        upload_to="images/profiles/",
    )
    speciality = models.CharField(
        verbose_name="вы по специальности",
        max_length=50,
        null=True,
        blank=True,
    )
    description = models.CharField(
        verbose_name="информация о вас и вашем опыте",
        max_length=1200,
        null=True,
        blank=True,
    )
    skills = ArrayField(
        models.CharField(
            max_length=32,
        ),
        verbose_name="ваши навыки",
        help_text="Cписок ваших навыков через запятую",
        null=True,
        blank=True,
    )
    country = models.CharField(
        verbose_name="страна",
        max_length=64,
        null=True,
        blank=True,
    )
    city = models.CharField(
        verbose_name="город",
        max_length=64,
        null=True,
        blank=True,
    )
    phone = models.CharField(
        verbose_name="телефон",
        help_text="Номер телефона в формате +7(812)000-00-00",
        max_length=64,
        null=True,
        blank=True,
    )
    balance = models.DecimalField(
        verbose_name="баланс",
        max_digits=10,
        decimal_places=2,
        default=0.0,
    )

    class Meta:
        ordering = ["id"]
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"

    def __str__(self):
        return self.username

    @property
    def full_name(self) -> str | None:
        return f"{self.first_name} {self.last_name}".strip()

    @property
    def location(self) -> str | None:
        if self.country and self.city:
            return f"{self.city}, {self.country}".strip()
        elif self.city:
            return self.city.strip()
        elif self.country:
            return self.country.strip()


class Action(models.Model):
    """
    Модель для хранения "действий" пользователя, направленных на другие модели в БД ("target").

    user: пользователь, совершивший действие
    verb: что было сделано; использовать константы из этой модели
    created: дата/время действия
    target_ct: модель "цели" действия
    target_id: ID связанного объекта "цели"
    target: поле для создания связи на основе двух предыдущих полей
    """

    VIEW_SERVICE = "просмотрена услуга"
    VIEW_PROJECT = "просмотрен проект"
    PLACE_ORDER = "размещен заказ"
    RECEIVE_ORDER = "получен заказ"
    CANCEL_ORDER = "отменен заказ"

    user = models.ForeignKey(
        verbose_name="пользователь",
        to=CustomUser,
        related_name="actions",
        on_delete=models.CASCADE,
    )
    verb = models.CharField(
        verbose_name="действие",
        max_length=64,
    )
    target_ct = models.ForeignKey(
        ContentType,
        blank=True,
        null=True,
        related_name="target_obj",
        on_delete=models.CASCADE,
    )
    target_id = models.PositiveIntegerField(
        null=True,
        blank=True,
    )
    target = GenericForeignKey(
        ct_field="target_ct",
        fk_field="target_id",
    )
    created = models.DateTimeField(
        verbose_name="время события",
        auto_now_add=True,
    )

    class Meta:
        verbose_name = "действие"
        verbose_name_plural = "действия"
        ordering = ["-created"]
