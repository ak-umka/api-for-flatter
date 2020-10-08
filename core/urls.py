from django.urls import path
from rest_framework.routers import DefaultRouter

from core.views import CarViewSet, FightViewSet, FederationViewSet, NewsViewSet

router = DefaultRouter()
router.register("cars", CarViewSet )
router.register("Fighter", FightViewSet)
router.register("Federation", FederationViewSet)
router.register("News", NewsViewSet)

urlpatterns = router.urls