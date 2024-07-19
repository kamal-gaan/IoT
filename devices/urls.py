from django.urls import include, path
from rest_framework import routers
from .views import (
    DevicesViewsSet,
    ReadViewSet,
    UserViewSet,
    CreateUserView,
    DevicesDateRangeViewSet,
    ReadsSummaryViewSet,
)
from devices import views

router = routers.DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"date-range", DevicesDateRangeViewSet)
router.register(r"add_devices", DevicesViewsSet, basename="add devices")
router.register(r"add_read", ReadViewSet, basename="add read")

urlpatterns = [
    path("", include(router.urls)),
    # path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("list-device-all", views.list_all_devices),
    path("list-device/<str:device_name>/", views.find_device_by_name),
    path("create-user/", CreateUserView.as_view()),
    path(
        "summary/",
        ReadsSummaryViewSet.as_view({"post": "summary"}),
        name="reads-summary",
    ),
]
