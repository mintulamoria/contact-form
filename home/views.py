from django.shortcuts import render, redirect
from django.views.generic import View, CreateView
from .models import Contact
from django.urls import reverse_lazy
from django.http import HttpResponse
from .forms import ContactForm

class ContactCreate(CreateView):
	model = Contact
	form_class = ContactForm
	success_url = reverse_lazy("contact")

def contact_list(request):
	contacts = Contacts.objects.all()
	return render(request, 'home:contact_list.html', {'contact':contacts})

#def successView(request):
#	return HttpResponse('home:contact_list')