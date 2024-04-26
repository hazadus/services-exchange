from django.contrib.auth.models import AbstractUser
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
