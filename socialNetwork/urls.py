from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name=""),
    path("login/", views.login, name="login"),
    path("register/", views.register, name="register"),
    path("feed/", views.feed, name="feed"),
    path("logout", views.LogoutUser, name="logout"),
]