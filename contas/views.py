from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime
from .models import Transacao
from .forms import TransacaoForm


def home(request):
    data = {}
    data['now'] = datetime.datetime.now()

    #html = "<html><body><h1>Ola</h1></body></html>" 
    return render(request, 'contas/home.html', data)


def listagem(request):
    data = {}
    data['transacoes'] = Transacao.objects.all()
    return render(request, 'contas/listagem.html', data)


def nova_transacao(request):
    data = {}
    form = TransacaoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('url_listagem')

    data['form'] = form
    return render(request, 'contas/form.html', data)


def update(request, pk):
    data = {}
    transacao = Transacao.objects.get(pk=pk)
    form = TransacaoForm(request.POST or None, instance=transacao)

    if form.is_valid():
        form.save()
        return redirect('url_listagem')

    data['form'] = form 
    data['transacao'] = transacao
    return render(request, 'contas/form.html', data)


def delete(request, pk):
    transacao = Transacao.objects.get(pk=pk).delete()
    return redirect('url_listagem')

