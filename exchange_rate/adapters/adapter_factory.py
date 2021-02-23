from ..constants import Providers
from . import FixerAdapter, MockAdapter


class AdapterFactory(object):

    @classmethod
    def getAdapter(cls, provider, source_currency, exchanged_currency):

        if provider == Providers.FIXER:
            return FixerAdapter(source_currency, exchanged_currency)

        if provider == Providers.MOCK:
            return MockAdapter(source_currency, exchanged_currency)

        return None
