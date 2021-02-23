from decimal import Decimal

from .base import AdapterBase


class FixerAdapter(AdapterBase):

    def adapt(self, data):
        return self.create_currency_exchange_rate(
            source=self.get_currency_by_code(self.source),
            exchange=self.get_currency_by_code(self.exchanged),
            rate_value=Decimal(data.get('rates').get(self.exchanged)),
            date=data.get('date'),
        )
