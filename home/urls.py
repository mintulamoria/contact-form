from django.urls import path
from .import views
from .views import ContactCreate

urlpatterns = [
#	path('', views.Contact, name='home'),
	path("", ContactCreate.as_view(), name="contact"),
#	path("", views.contacts, name='contact_list')
]