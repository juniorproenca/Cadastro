from django.shortcuts import render
from django.http import HttpResponse
import datetime 
from .forms import *
# Create your views here.

def home (request):	
	return render(request,'polls/home.html')

def inscrição(request):	
	form = UsuarioForm()
	return render(request,"polls/inscrição.html", {'form':form})


def cadastrar_usuario(request):
    form = UsuarioForm()
    return render(request, 'form.html', {'form':form})