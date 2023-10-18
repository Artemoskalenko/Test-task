from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from .views import login, signout, main_page
from api.views import PersonViewSet, TeamViewSet


router = routers.DefaultRouter()
router.register(r'person', PersonViewSet)
router.register(r'team', TeamViewSet)


urlpatterns = [
    path("admin/logout/", signout),
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("login/", login, name="login"),
    path("", main_page),

    path('api/v1/', include(router.urls)),
]
