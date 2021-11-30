from django.contrib import admin
from main.models import BitCoinToUSD

# Register your models here.

class BitCoinToUSDAdmin(admin.ModelAdmin):
    class Meta:
        model = BitCoinToUSD

    list_display = ['id', 'exchange_rate', 'last_refreshed']

admin.site.register(BitCoinToUSD, BitCoinToUSDAdmin)
