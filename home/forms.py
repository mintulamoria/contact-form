from django import forms
from django.forms import ModelForm, Textarea
from .models import Contact


# Create your forms here.

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ["first_name", "last_name", "message", "mobile_number"]
        