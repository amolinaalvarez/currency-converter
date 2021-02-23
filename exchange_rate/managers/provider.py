from django.db import models

from ..querysets import PrividerQuerySet


class ProviderManager(models.Manager):

    queryset_class = PrividerQuerySet

    def get_queryset(self):
        return self.queryset_class(self.model, using=self._db)
