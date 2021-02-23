from datetime import date
from decimal import Decimal

from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response

from ..serializers import CurrencyConverterSerializer
from ..models import CurrencyConverter
from ...models import CurrencyExchangeRate, Provider
from ...exchange_manager import get_exchange_rate_data


class CurrencyConverterView(GenericViewSet):

    serializer_class = CurrencyConverterSerializer
    model = CurrencyConverter

    @action(detail=False, methods=['GET'], url_path='calculate')
    def calculate(self, request):
        # TODO: validate GET params
        source_code = self.request.GET.get('source_currency', None)
        exchanged_code = self.request.GET.get('exchanged_currency', None)
        amount = self.request.GET.get('amount', None)
        # Check if there is any existed object for the request
        rates = CurrencyExchangeRate.objects.filter_by_date(date.today()).filter_by_source_and_exchanged_currency_code(
            source_code, exchanged_code)
        if rates:
            rate = rates.first()
        else:
            # Take the provider which has the highest priority
            provider = Provider.objects.order_by('priority').first()
            rate = get_exchange_rate_data(source_code, exchanged_code, date.today(), provider.name)

        response = self.model(
                source_code=source_code,
                exchanged_code=exchanged_code,
                amount=amount,
                result=rate.get_conversion(Decimal(amount)))
        serializer = self.serializer_class(response)
        return Response(serializer.data, status.HTTP_200_OK)
