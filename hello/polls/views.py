from django.shortcuts import render
from django.http import HttpResponse
import datetime 
# Create your views here.

def home (request):	
	return render(request,'polls/home.html')

def inscrição(request):	
	return render(request,'polls/inscrição.html')