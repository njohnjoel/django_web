from django.urls import path
from src.intranet1.myapp import views

urlpatterns = [
    path('', views.home, name='home'),
]