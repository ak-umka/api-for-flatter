from django.http import JsonResponse
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework import generics, filters
from core.models import Car, Fighter, Federation, News
from core.serializers import CarSerializer, FighterSerializer, FederationSerializer, NewsSerializer, UserSerializer, LoginSerializer
from django.contrib.auth.models import User
from rest_framework import permissions
# from core.permissons import IsOwnerOrReadOlny
from rest_framework.views import APIView
from django.contrib.auth import login as django_login, logout as django_logout
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer = UserSerializer

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
    search_fields = ['title', 'author']
    filter_backends = (filters.SearchFilter, )
    serializer_class = NewsSerializer
    queryset = News.objects.all()
    # permission_classes = [permissions.IsAdminUser,]

    def get_queryset(self):
        return News.objects.filter(owner=self.request.user.id)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validate_data["user"]
        django_login(request, user)
        token, created = Token.objects.get_or_create()
        return Response({"token":token.key}, status=200)
        

class LogoutView(APIView):
    authentication_classes =(TokenAuthentication,)
    def post(self, request):
        django_logout(request)
        return Response(status=204)