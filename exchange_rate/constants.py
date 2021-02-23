
class Providers(object):
    FIXER = "Fixer"
    MOCK = "Mock"

    PROVIDERS = (
        FIXER,
        MOCK
    )

    @classmethod
    def get_provider_from_string(cls, provider_name):
        if provider_name in cls.PROVIDERS:
            return provider_name
        return None
