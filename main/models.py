from django.db import models

# Create your models here.

class BitCoinToUSD(models.Model):
    exchange_rate = models.DecimalField(decimal_places=10, max_digits=100)
    last_refreshed = models.CharField(max_length=60)
