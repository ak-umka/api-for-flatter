from django.http import JsonResponse
from rest_framework.viewsets import ViewSet, ModelViewSet

from core.models import Car, Fighter, Federation, News
from core.serializers import CarSerializer, FighterSerializer, FederationSerializer, NewsSerializer

class CarViewSet(ModelViewSet):
    serializer_class = CarSerializer
    queryset = Car.objects.all()

class FightViewSet(ModelViewSet):
    serializer_class = FighterSerializer
    queryset = Fighter.objects.all()

class FederationViewSet(ModelViewSet):
    serializer_class = FederationSerializer
    queryset = Federation.objects.all()

class NewsViewSet(ModelViewSet):
    serializer_class = NewsSerializer
    queryset = News.objects.all()
