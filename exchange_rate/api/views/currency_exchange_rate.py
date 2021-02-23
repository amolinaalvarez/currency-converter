from rest_framework.generics import ListAPIView

from ...models import CurrencyExchangeRate
from ..serializers import CurrencyExchangeRateSerializer


class CurrencyExchangeRateListView(ListAPIView):

    model = CurrencyExchangeRate
    serializer_class = CurrencyExchangeRateSerializer

    def get_queryset(self):
        # TODO: validate GET params
        source_currency = self.request.GET.get('source_currency', None)
        date_from = self.request.GET.get('date_from', None)
        date_to = self.request.GET.get('date_to', None)
        if not (source_currency or date_from or date_to):
            return self.model.objects.all()
        return self.model.objects.filter_by_date_range(date_from, date_to).filter_by_source_currency_code(
            source_currency)
