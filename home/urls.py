from django.urls import path
from .views import login_page, login_view, register

urlpatterns = [
    path('', login_page, name='index'),
    path('login/', login_view, name='login'),
    path('register/', register, name='register'),

]
