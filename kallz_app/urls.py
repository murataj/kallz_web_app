from django.urls import path, include
from kallz_app import views
from django.http import HttpResponse

urlpatterns = [

    path('', views.home),
    path("classes/", views.classes, name="register"),
    path("register/", views.registerPage, name="register"),
    path("register/", views.registerPage, name="register"),
    path("login/", views.loginPage, name="login"),
    path("logout/", views.logoutUser, name="logout"),
    path("user/", views.userPage, name="user-page"),
    path("index/", views.index, name="index"),

]