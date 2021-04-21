from django.urls import path
from django.urls import include
from .views import youtube

urlpatterns = [
    path('', youtube)
]