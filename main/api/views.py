from rest_framework import viewsets, status
from rest_framework.response import Response

from main.api.serializers import BitCoinToUSDSerializer
from main.models import BitCoinToUSD
from main.services import get_bitcoin_exchange

class BitCoinToUSDViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be view currency exchange
    """
    queryset = BitCoinToUSD.objects.all().order_by('-id')
    serializer_class = BitCoinToUSDSerializer

    def create(self, request, *args, **kwargs):
        success = get_bitcoin_exchange()
        if success:
            new_exchanges = self.get_queryset()
            serializer = BitCoinToUSDSerializer(new_exchanges, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'error': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)
