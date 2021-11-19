from django.urls import path
from .views import *

urlpatterns = [
    path('', Home, name='Home'),
    path('music/<str:pk>/', singleMusic, name='single-music'),
    path('category/<str:pk>/', categoryPage, name='category-page'),
]