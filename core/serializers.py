from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from core.models import Car, Fighter, Federation, News
from django.contrib.auth.models import User


class UserSerializer(ModelSerializer):
    news = serializers.PrimaryKeyRelatedField(many=True, queryset = News.objects.all)
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = User
        fields = "__all__"

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

class LoginSerializer():
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get("username", "")
        password = data.get("password", "")

        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    data["user"] = user
                else:
                    msg = "user is deactivated"
                    raise exceptions.ValidationError(msg)
            else:
                msg = "Unable to login with given credentials."
                raise exceptions.ValidationError(msg)
        else:
            msg = "Must provide username and password both."
            raise exceptions.ValidationError(msg)
        return data
