from datetime import date


class MockClient(object):

    def latest(self, base, symbols):
        # TODO: generate a ramdom value for 'rate'
        return {
            'source': 'USD',
            'exchanged': 'EUR',
            'date': date.today().strftime('%Y-%m-%d'),
            'rate': 0.72007
        }
