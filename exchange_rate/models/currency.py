from django.db import models

from ..conf import settings


class Currency(models.Model):
    code = models.CharField(
        max_length=3,
        unique=True,
        blank=False, null=False,
        choices=settings.EXCHANGE_RATE_CH_CURRENCY_CODE,
    )

    name = models.CharField(
        blank=False, null=False,
        max_length=20,
        db_index=True
    )

    symbol = models.CharField(max_length=10)

    def __str__(self):
        return '{} ({})'.format(self.name, self.code)
