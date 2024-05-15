from django.urls import path
from . import views

""" URL patterns for webapp. """
urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('authentication/', views.user_login, name='user_login'),
]