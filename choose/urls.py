from django.urls import path
from . import views

add_name = 'choose'

urlpatterns = [
    path('', views.index),
]