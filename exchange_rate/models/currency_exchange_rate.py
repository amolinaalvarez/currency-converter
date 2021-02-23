from django.db import models

from model_utils.models import TimeStampedModel

from ..managers import CurrencyExchangeRateManager


class CurrencyExchangeRate(TimeStampedModel):
    source_currency = models.ForeignKey(
        'exchange_rate.Currency',
        related_name='exchanges',
        on_delete=models.CASCADE)

    exchanged_currency = models.ForeignKey(
        'exchange_rate.Currency',
        on_delete=models.CASCADE)

    valuation_date = models.DateField(db_index=True)

    rate_value = models.DecimalField(
        db_index=True,
        decimal_places=6,
        max_digits=18)

    objects = CurrencyExchangeRateManager()

    def __str__(self):
        return '{} - {} : {} ({})'.format(
            self.source_currency,
            self.exchanged_currency,
            self.rate_value,
            self.valuation_date
        )

    def get_conversion(self, amount):
        return self.rate_value * amount
