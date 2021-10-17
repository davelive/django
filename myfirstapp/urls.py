from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='myfirstapp-home'),
    path('about/', views.about, name='about-page')
]
