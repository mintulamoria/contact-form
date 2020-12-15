from django import forms
from django.forms import ModelForm
from .models import Contact


class ContactForm(ModelForm):
	class Meta:
		model = Contact
		fields = ["first_name", "last_name", "message", "mobile_number"]