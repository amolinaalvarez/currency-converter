from .adapters import AdapterFactory
from .clients import ClientFactory


def get_exchange_rate_data(source_currency, exchanged_currency, valuation_date, provider):
    client = ClientFactory.getClient(provider)
    # TODO: manage exceptions from the external api
    response = client.latest(source_currency, [exchanged_currency])
    adapter = AdapterFactory.getAdapter(provider, source_currency, exchanged_currency)
    new_rate = adapter.adapt(response)
    return new_rate
