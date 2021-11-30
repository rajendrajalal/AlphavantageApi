import os
from decimal import Decimal

import requests
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AlphavantageApi.settings')

app = Celery('AlphavantageApi')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


@app.task(bind=True)
def get_bitcoin_exchange(*args, **kwargs):
    from main.models import BitCoinToUSD
    x_rapidapi_key = os.environ.get('RAPIDAPIKEY')
    if not x_rapidapi_key:
        return False
    url = "https://alpha-vantage.p.rapidapi.com/query"

    querystring = {"from_currency": "BTC", "function": "CURRENCY_EXCHANGE_RATE", "to_currency": "USD"}

    headers = {
        'x-rapidapi-key': x_rapidapi_key,
        'x-rapidapi-host': "alpha-vantage.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers, params=querystring).json()
    exchange_rate = response['Realtime Currency Exchange Rate']['5. Exchange Rate']
    last_refreshed = response['Realtime Currency Exchange Rate']['6. Last Refreshed']
    new_exchange = BitCoinToUSD(exchange_rate=Decimal(exchange_rate), last_refreshed=last_refreshed)
    new_exchange.save()
    return True
