from django.conf.urls import include, url
from rest_framework import routers

from main.api import views

router = routers.DefaultRouter()
router.register(r'quotes', views.BitCoinToUSDViewSet, basename='bitcointousd')

urlpatterns = [
    # urls for Django Rest Framework API
    url('^', include(router.urls)),
]