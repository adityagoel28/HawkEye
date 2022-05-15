from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('video/', views.video),
    path('transcript/', views.transcript, name='transcript'),
    path('upload/', views.upload),
    path('search/', views.keywordSearch),
]