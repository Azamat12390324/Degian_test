from django.shortcuts import render
from django.views.generic import TemplateView
from main.models import Home, About, Services, Contact

class HomeView(TemplateView):
    model = Home
    template_name = 'layouts/base.html'


class AboutView(TemplateView):
    model = About
    template_name = 'about.html'

class ServicesView(TemplateView):
    model = Services
    template_name = 'service.html'

class ContactView(TemplateView):
    model = Contact
    template_name = 'contact.html'

