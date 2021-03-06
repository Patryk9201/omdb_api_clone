from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter
from django.urls import path, include
from omdb_api.users.api.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)


app_name = "APII"
urlpatterns = [path('', include('APII.urls')), ]
urlpatterns += router.urls

