from django.test import TestCase

from ..models import CurrencyExchangeRate
from .fixer import FixerAdapter


class FixerAdapterTest(TestCase):

    fixtures = ['currencies.json']

    def setUp(self):
        self.source_currency = 'USD'
        self.exchanged_currency = 'GBP'
        self.api_response = self.setup_latest_rate_api_response()

    def setup_latest_rate_api_response(self):
        return {
            'success': 'true',
            'timestamp': 1519296206,
            'base': self.source_currency,
            'date': '2021-02-23',
            'rates': {
                self.exchanged_currency: 0.72007
            }
        }

    def test_adapt(self):
        rates = CurrencyExchangeRate.objects.all()
        self.assertEqual(rates.count(), 0)
        new_rate = FixerAdapter(self.source_currency, self.exchanged_currency).adapt(
            self.api_response)
        self.assertIsNotNone(new_rate)
        self.assertEqual(CurrencyExchangeRate.objects.count(), 1)
