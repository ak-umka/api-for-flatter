from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include("core.urls")),
    path('fighters/', include("core.urls")),
    path('federation/', include("core.urls")),
    path('news/', include("core.urls")),
]
