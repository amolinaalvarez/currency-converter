from django.conf.urls import url, include

app_name = 'api'

urlpatterns = [
    url(r'^currency-exchanges/', include('exchange_rate.api.urls'))
]
