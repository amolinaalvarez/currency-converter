from django.conf.urls import url, include
from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import CurrencyExchangeRateListView, CurrencyConverterView

router = DefaultRouter()
router.register(r'', CurrencyConverterView, basename='')

urlpatterns = [
    url(r'^list/', CurrencyExchangeRateListView.as_view(), name='list'),
    path('', include(router.urls)),
]
