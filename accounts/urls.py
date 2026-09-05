from django.urls import path
from . import views


urlpatterns = [
    path("signup/", views.signup_view, name="worker-signup"),
    path("login/", views.login_view, name="worker-login"),
    path("logout/", views.logout_view, name="worker-logout"),
]