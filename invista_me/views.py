from django.shortcuts import render # redenrizar pagina html
from django.shortcuts import HttpResponse, redirect # importado por mim
from .models import Investimento
from .forms import InvestimentoForm  # importando o formulario para criar elementos
from django.contrib.auth.decorators import login_required  # limitando os usuarios nao logados para paginas selecionadas





def investimentos(request):
    dados = {
        'dados' : Investimento.objects.all()
    }
    return render(request,'investimentos/investimentos.html', context=dados)


@login_required
def detalhe(request, id_investimento):
    dados = {
        'dados': Investimento.objects.get(pk=id_investimento)
    }
    return render(request,'investimentos/detalhe.html', context=dados)


@login_required
def criar(request):
    if request.method == 'POST':
        investimento_form = InvestimentoForm(request.POST)
        if investimento_form.is_valid():
            investimento_form.save()
            return redirect('investimentos') # é o que corresponde ao name em urls.py
    investimento_form = InvestimentoForm()
    formulario = {
        'formulario' : investimento_form
    }
    return render(request, 'investimentos/novo_investimento.html', context=formulario)

@login_required
def editar(request,id_investimento):
    investimento = Investimento.objects.get(pk=id_investimento)
    if request.method == 'GET':
        formulario = InvestimentoForm(instance=investimento)
        return render(request, 'investimentos/novo_investimento.html', {'formulario': formulario})
    elif request.method == 'POST':
        formulario = InvestimentoForm(request.POST, instance=investimento)
        if formulario.is_valid():
            formulario.save()
        return redirect('investimentos')
    

@login_required
def excluir(request, id_investimento):
    investimento = Investimento.objects.get(pk=id_investimento)
    if request.method == 'POST':
        investimento.delete()
        return redirect('investimentos')
    return render(request, 'investimentos/confirmar_exclusao.html', {'item': investimento})

def base(request):
    return render(request,'investimentos/base.html')


