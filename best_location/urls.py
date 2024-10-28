from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("try_AI", views.try_AI, name="try_AI"),
    path('result/<int:input_id>/', views.result_view, name='result'),
    path('archive/', views.archive, name='archive'),
    path('delete/<int:pk>/', views.delete_information, name='delete_information'),
    ]
