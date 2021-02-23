from django.contrib import admin

from .models import (Currency, CurrencyExchangeRate, Provider)

admin.site.register(Currency)
admin.site.register(CurrencyExchangeRate)
admin.site.register(Provider)
