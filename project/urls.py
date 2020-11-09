from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from core.views import CarViewSet, FightViewSet, FederationViewSet, NewsViewSet, LoginView, LogoutView

router = routers.DefaultRouter()
router.register("cars", CarViewSet )
router.register("Fighter", FightViewSet)
router.register("Federation", FederationViewSet)
router.register("News", NewsViewSet)
# urlpatterns = router.urls

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    # path('api/', include("core.urls")),
    # path('api-f/', include("core.urls")),
    # path('fighters/', include("core.urls")),
    # path('federation/', include("core.urls")),
    # path('news/', include("core.urls")),
    path('accounts/', include('allauth.urls')),
    path('api/login/', LoginView.as_view()),
    path('api/logout/', LogoutView.as_view()),
]   

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)