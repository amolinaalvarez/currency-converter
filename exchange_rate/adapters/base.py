
from abc import ABC, abstractmethod

from ..models import CurrencyExchangeRate, Currency


class AdapterBase(ABC):

    def __init__(self, source, exchanged):
        self.source = source
        self.exchanged = exchanged
        super().__init__()

    @abstractmethod
    def adapt(self, data):
        pass

    def get_currency_by_code(self, code):
        return Currency.objects.get(code=code)

    def create_currency_exchange_rate(self, source, exchange, rate_value, date):
        currency_exchange_rate, _ = CurrencyExchangeRate.objects.update_or_create(
                source_currency=source,
                exchanged_currency=exchange,
                valuation_date=date,
                defaults={'rate_value': rate_value})

        return currency_exchange_rate
