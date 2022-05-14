from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('video/', views.video)
]
