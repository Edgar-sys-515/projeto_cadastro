from django.shortcuts import render, redirect # redenrizar pagina html,
from django.shortcuts import HttpResponse, redirect # importado por mim
#from django.contrib.auth.forms import UserCreationForm # isso tem pronto no django para criação de usuarios
from django.contrib import messages
from .forms import UserRegisterForm


# Create your views here.

def novo_usuario(request):
    # tipo, validar, informar, salvar
    if request.method == 'POST':
        #formulario = UserCreationForm(request.POST)  # populando a classe com o POST
        formulario = UserRegisterForm(request.POST)  # populando a classe com o POST, userreggisterform criamos no arquivo forms parar alterar informações do formulario
        if formulario.is_valid():
            formulario.save()
            #informar
            usuario = formulario.cleaned_data.get('username')  # username pois pegamos as informação em f12, .clean_data.get() é para pegar todas as informações do formulario
            messages.success(request,f'Usuário de {usuario} foi criado com sucesso!')
            return redirect('login')
        
    else:
        formulario = UserRegisterForm() # formulario vazio

    return render(request,'usuarios/registrar.html', {'formulario':formulario})


# tipo de mensagem
'''
messages.debug
        .info
        sucess
        warning
        error

'''

