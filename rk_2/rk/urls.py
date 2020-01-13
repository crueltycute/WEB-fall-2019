from django.urls import path
from . import views


app_name = 'rk'
urlpatterns = [
    path('', views.index),
]