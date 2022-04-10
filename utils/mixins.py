from django.db import models


class NameDescriptionMixin(models.Model):
    name = models.CharField(
        max_length=150,
    )
    description = models.CharField(
        default="",
        blank=True,
        max_length=254,
    )

    class Meta:
        abstract = True


class CreatedModifiedDtMixin(models.Model):
    created_dt = models.DateTimeField(
        auto_now_add=True,
    )
    modified_dt = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        abstract = True
