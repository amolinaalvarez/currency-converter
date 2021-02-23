from django.conf import settings  # noqa

from appconf import AppConf


class ExchangeRateConfig(AppConf):

    CH_CURRENCY_USD_DOLLAR = 'USD'
    CH_CURRENCY_EURO = 'EUR'
    CH_CURRENCY_SWISS_FRANC = 'CHF'
    CH_CURRENCY_BRITISH_POUND = 'GBP'

    CH_CURRENCY_CODE = (
        (CH_CURRENCY_USD_DOLLAR, 'US Dollar'),
        (CH_CURRENCY_SWISS_FRANC, 'Swiss Franc'),
        (CH_CURRENCY_EURO, 'Euro'),
        (CH_CURRENCY_BRITISH_POUND, 'British Pound')
    )
