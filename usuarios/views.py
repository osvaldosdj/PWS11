from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from django.contrib.messages import constants

# Create your views here.

def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    
    elif request.method == "POST":
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')
        print(request.POST)

        if not senha == confirmar_senha:
            messages.add_message(request, constants.ERROR, "As senhas não são iguais")
            return redirect ('cadastro')
        
        if len(senha) < 6:
            messages.add_message(request, constants.ERROR, "As senhas precisam de 6 dígitos mínimos")
            return redirect('cadastro/')
        
        users = User.objects.filter(username=username)

        if users.exists():
            messages.add_message(request, constants.ERROR, "Usuário já existe")
            return redirect ('cadastro')


        user = User.objects.create_user(
            username=username,
            password=senha
        )

        return redirect ('/usuarios/logar')
    

def logar(request):
    if request.method == "GET":
        return render(request, 'logar.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = auth.authenticate(request, username=username, password=senha)

        if user:
            auth.login(request, user)
            return redirect('/home') # Vai dar erro

        messages.add_message(request, constants.ERROR, 'Usuario ou senha inválidos')
        return redirect('/usuarios/logar')