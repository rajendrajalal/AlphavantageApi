from rest_framework import serializers

from main.models import BitCoinToUSD


class BitCoinToUSDSerializer(serializers.ModelSerializer):
    class Meta:
        model = BitCoinToUSD
        fields = ('pk', 'exchange_rate', 'last_refreshed')