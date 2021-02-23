from django.db import models


class CurrencyExchangeRateQuerySet(models.QuerySet):

    def filter_by_date_range(self, date_from, date_to):
        return self.filter(valuation_date__range=[date_from, date_to])

    def filter_by_date(self, date):
        return self.filter(valuation_date=date)

    def filter_by_source_currency_code(self, source_currency):
        return self.filter(source_currency__code=source_currency)

    def filter_by_source_and_exchanged_currency_code(self, source_currency, exchanged_currency):
        return self.filter(source_currency__code=source_currency, exchanged_currency__code=exchanged_currency)
