from django.db import models

from model_utils.models import TimeStampedModel

from ..managers import ProviderManager


class Provider(TimeStampedModel):
    name = models.CharField(
        blank=False, null=False,
        max_length=20,
        db_index=True
    )

    priority = models.IntegerField(
        blank=False, null=False)

    objects = ProviderManager()

    class Meta:
        ordering = ['priority']

    def __str__(self):
        return '{} : {}'.format(self.name, self.priority)
