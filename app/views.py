from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from app.forms import FormUsuario
# Create your views here.

def app(request):
    pagina_config = Pagina.objects.first()
    return render(request, 'home.html', {"pagina":pagina_config})

def sobre(request):
    return render(request, 'sobre.html')

def produtos(request):

    produtos = Produto.objects.all()
    return render(request,'produtos.html',{"produtos": produtos})

def salvarUsuario(request):
    formulario = FormUsuario(request.POST or None)
    if request.POST:
        if formulario.is_valid():
            # Cria mas não salva no banco
            usuario = formulario.save(commit=False)

            # Criptografa a senha
            usuario.set_password(formulario.cleaned_data['password1'])

            usuario.save()
            return redirect('loginUsuario')
    return render(request, "salvarUsuario.html", {'form':formulario})

def loginUsuario(request):
    if request.POST:
        nome = request.POST.get('nome')
        senha = request.POST.get('senha')
        usuario = authenticate(request, username=nome, password=senha)
        
        if usuario is not None:
            login(request, usuario)
            return redirect('dashboard')
        else:
            messages.error(request, "Usuário ou senha incorretos")
    return render(request,'login.html')

@login_required(login_url='loginUsuario')
def dashboard(request):
    if not request.user:
        return redirect("loginUsuario")
    return render(request, "dashboard.html", {"usuario":request.user})

        