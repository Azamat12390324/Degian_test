from django.urls import path
from main.views import HomeView, AboutView, ContactView, ServicesView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path("", AboutView.as_view(), name='about'),
    path("", ContactView.as_view(), name='contact'),
    path("",ServicesView.as_view(), name='service')
]    
