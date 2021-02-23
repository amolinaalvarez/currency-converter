from django.db import models

from ..querysets import CurrencyExchangeRateQuerySet


class CurrencyExchangeRateManager(models.Manager):

    queryset_class = CurrencyExchangeRateQuerySet

    def get_queryset(self):
        return self.queryset_class(self.model, using=self._db)

    def filter_by_date_range(self, date_from, date_to):
        return self.get_queryset().filter_by_date_range(date_from, date_to)

    def filter_by_date(self, date):
        return self.get_queryset().filter_by_date(date)

    def filter_by_source_currency_code(self, source_currency):
        return self.get_queryset().filter_by_source_currency_code(source_currency)

    def filter_by_source_and_exchanged_currency_code(self, source_currency, exchange_currency):
        return self.get_queryset().filter_by_source_and_exchanged_currency_code(source_currency, exchange_currency)
