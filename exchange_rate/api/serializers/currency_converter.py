from rest_framework import serializers


class CurrencyConverterSerializer(serializers.Serializer):
    source_code = serializers.CharField(max_length=3)
    exchanged_code = serializers.CharField(max_length=3)
    amount = serializers.DecimalField(decimal_places=6, max_digits=18)
    result = serializers.DecimalField(decimal_places=6, max_digits=18)
