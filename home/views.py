from django.shortcuts import render, redirect
from django.views.generic import View, CreateView
from .models import Contact
from django.core.mail import send_mail, BadHeaderError
from django.urls import reverse_lazy
from django.http import HttpResponse
from .forms import ContactForm

class ContactCreate(CreateView):
	model = Contact
	form_class = ContactForm
	success_url = reverse_lazy("contact")

class ContactView(CreateView):
	template_name = 'contact_form.html'

	def get_contact_data(self, **kwargs):
		contact = super(ContactView, self).get_contact_data(**kwargs)
		contact['object_list'] = UserList.objects.all()
		return contact