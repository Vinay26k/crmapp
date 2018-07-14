from django.shortcuts import render
from django.views.generic.base import TemplateView
# Create your views here.

class HomePage(TemplateView):
	"""
		Because our needs are so simple,
		we will assign one value; template name
	"""
	template_name = 'marketing/home.html'