from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("try_AI", views.try_AI, name="try_AI"),
    path('result/<int:input_id>/', result_view, name='result'),
    ]
