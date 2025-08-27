from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from users.views import (
    PaymentCreateAPIView,
    PaymentDestroyAPIView,
    PaymentListAPIView,
    PaymentRetrieveAPIView,
    PaymentUpdateAPIView,
    SubscriptionAPIView,
    UserCreateAPIView,
    UserViewSet,
)

app_name = UsersConfig.name

router = SimpleRouter()
router.register("users", UserViewSet)

urlpatterns = [
    path("register/", UserCreateAPIView.as_view(), name="register"),
    path("payment/", PaymentListAPIView.as_view(), name="payment_list"),
    path(
        "payment/<int:pk>/", PaymentRetrieveAPIView.as_view(), name="payment_retrieve"
    ),
    path("payment/create/", PaymentCreateAPIView.as_view(), name="payment_create"),
    path("payment/<int:pk>/", PaymentDestroyAPIView.as_view(), name="payment_destroy"),
    path("payment/<int:pk>/", PaymentUpdateAPIView.as_view(), name="payment_update"),
    path(
        "login",
        TokenObtainPairView.as_view(permission_classes=(AllowAny,)),
        name="login",
    ),
    path(
        "token/refresh/",
        TokenRefreshView.as_view(permission_classes=(AllowAny,)),
        name="token_refresh",
    ),
    path("sub/", SubscriptionAPIView.as_view(), name="subscription"),
]

urlpatterns += router.urls
