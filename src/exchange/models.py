from django.db import models


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
        indexes = [
            models.Index(fields=["title"]),
        ]
        verbose_name = "категория"
        verbose_name_plural = "категории"

    def __str__(self):
        title = self.title
        parent = self.parent
        while parent:
            title = f"{parent.title} / {title}"
            parent = parent.parent
        return title
