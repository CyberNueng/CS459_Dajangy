from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import datetime
from .models import Person
from .forms import PersonForm
from django.views.generic.edit import CreateView

class CreatePersonView(CreateView):
	queryset = Person()
	template_name='create.html'
	form_class = PersonForm
	success_url = '/list'