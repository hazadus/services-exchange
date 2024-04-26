# Generated by Django 5.0.4 on 2024-04-26 18:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("exchange", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Service",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=70, verbose_name="название")),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="images/services/",
                        verbose_name="обложка",
                    ),
                ),
                (
                    "description",
                    models.CharField(
                        help_text="Подробное описание предрставляемой услуги",
                        max_length=1200,
                        verbose_name="описание",
                    ),
                ),
                (
                    "required",
                    models.CharField(
                        help_text="Укажите что требуется от заказчика услуги. Например, ТЗ, доступы, и т.п.",
                        max_length=500,
                        verbose_name="от покупателя нужно",
                    ),
                ),
                (
                    "price",
                    models.IntegerField(
                        help_text="Стоимость услуги в руб.", verbose_name="стоимость"
                    ),
                ),
                (
                    "term",
                    models.IntegerField(
                        help_text="Срок выполнения услуги, в днях", verbose_name="срок"
                    ),
                ),
                (
                    "options",
                    models.CharField(
                        blank=True,
                        help_text="Если вы предлагаете дополнительные услуги, расскажите о них. Укажите название, срок, стоимость.",
                        max_length=1200,
                        null=True,
                        verbose_name="дополнительные услуги",
                    ),
                ),
                (
                    "portfolio_url",
                    models.URLField(
                        blank=True, null=True, verbose_name="ссылка на портфолио"
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Снимите галочку, чтобы исключить услугу из каталога, не удаляя её.",
                        verbose_name="услуга активна",
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(auto_now_add=True, verbose_name="создана"),
                ),
                (
                    "updated",
                    models.DateTimeField(auto_now=True, verbose_name="изменена"),
                ),
                (
                    "category",
                    models.ForeignKey(
                        help_text="Категория, в которой будет размещена услуга",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="services",
                        to="exchange.category",
                        verbose_name="рубрика",
                    ),
                ),
            ],
        ),
    ]
