import requests

from .exceptions import FixerException


class FixerClient(object):

    BASE_URL = 'http://data.fixer.io/api/'

    LATEST_PATH = 'latest'

    def __init__(self, access_key):
        self.access_key = access_key

    def _create_payload(self, base, symbols):
        payload = {'access_key': self.access_key}
        # FIXME: basic plan is requerid in order to use 'base' param :(
        # payload['base'] = base
        payload['symbols'] = ','.join(symbols)
        return payload

    def latest(self, base, symbols):
        try:
            payload = self._create_payload(base, symbols)
            url = self.BASE_URL + self.LATEST_PATH
            response = requests.get(url, params=payload)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as ex:
            raise FixerException(str(ex))
