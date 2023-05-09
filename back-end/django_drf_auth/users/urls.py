from django.urls import path
from .views import RegistrationView, LoginView, ChangePasswordView, RegisterView, UserView, profileInfo, prefTech
from rest_framework_simplejwt.views import token_refresh

app_name = "users"

urlpatterns = [
    path("register/", RegistrationView.as_view(), name="register"),
    path('register-update/', RegisterView.as_view(), name="register-update"),
    path("login/", LoginView.as_view(), name="login"),
    path("change-password/", ChangePasswordView.as_view(), name="change_password"),
    path("token-refresh/", token_refresh, name="token_refresh"),
    path('user/', UserView.as_view()),
    path('pref-tech/', prefTech.as_view()),

    path('user-profile/', profileInfo.as_view()),
]
