from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Produto
# Create your views here.

def app(request):
    return render(request, 'home.html')

def sobre(request):
    return render(request, 'sobre.html')

def produtos(request):

    produtos = Produto.objects.all()
    return render(request,'produtos.html',{"produtos": produtos})