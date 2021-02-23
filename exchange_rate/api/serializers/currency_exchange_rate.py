from rest_framework import serializers

from ...models import CurrencyExchangeRate


class CurrencyExchangeRateSerializer(serializers.ModelSerializer):

    source_currency = serializers.CharField(source='source_currency.code')
    exchanged_currency = serializers.CharField(source='exchanged_currency.code')

    class Meta:
        model = CurrencyExchangeRate
        fields = ['source_currency', 'exchanged_currency', 'rate_value', 'valuation_date']
