from django.urls import path
from .views import UserView, UserIdView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [path("users/", UserView.as_view()),
               path("users/login/", TokenObtainPairView.as_view()),
               path("users/refresh", TokenRefreshView.as_view()),
               path("users/<int:user_id>/", UserIdView.as_view())
               ]