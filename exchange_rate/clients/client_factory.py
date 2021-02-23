from django.conf import settings

from ..constants import Providers
from . import (FixerClient, MockClient)


class ClientFactory(object):

    @classmethod
    def getClient(cls, provider):

        if provider == Providers.FIXER:
            return FixerClient(access_key=settings.FIXER_API_ACCESS_KEY)

        if provider == Providers.MOCK:
            return MockClient()

        return None
