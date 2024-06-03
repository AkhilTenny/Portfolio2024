
from django.urls import path 
from portfolio.views import home,contact

urlpatterns = [
    path('',home ),
    path('contact/',contact)
]
