from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
	print(HttpResponse("Hello World"))
	response = HttpResponse("Hello World") 
