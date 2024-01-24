from django.urls import path
from .views import webcam

urlpatterns = [
    path('', webcam, name='webcam'),
]