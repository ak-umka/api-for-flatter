from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from core.models import Car, Fighter, Federation, News


class CarSerializer(ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"

class FighterSerializer(ModelSerializer):
    class Meta:
        model = Fighter
        fields = "__all__"

class FederationSerializer(ModelSerializer):
    class Meta:
        model = Federation
        fields = "__all__"

class NewsSerializer(ModelSerializer):
    publication_date = serializers.DateField(format="%d-%m-%Y", input_formats=['%d-%m-%Y', 'iso-8601'])
    class Meta:
        model = News
        fields = "__all__"

