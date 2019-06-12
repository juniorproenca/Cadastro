from django.shortcuts import render
from django.http import HttpResponse
import datetime 
from .forms import *
from django.urls import path

from django.views.generic import TemplateView
# Create your views here.

class homeTemplateView(TemplateView):	
	template_name= "polls/home.html"
	
def inscrição(request):	
 	form = UsuarioForm()

 	if form.is_valid():
 		form.save()
 		return listagem(request)
 	return render(request,"polls/inscrição.html", {'form':form})


def listagem(request):
 	lista={}
 	lista ['listas'] = Usuario.objects.all()
 	return render(request, 'polls/listagem.html',lista)