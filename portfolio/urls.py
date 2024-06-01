
from django.urls import path
from portfolio.views import home

urlpatterns = [
    path('',home, name='home' ),
]
