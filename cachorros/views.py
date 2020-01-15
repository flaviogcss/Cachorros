from django.shortcuts import render

# Create your views here.

from cachorros.forms import CachorroForm


def cadastro(request):
    form = cachorrosForm(request.POST or None)
    args = {
        'form':form
    }
    if form.is_valid():
            form.save()
            args['msg'] = 'Cadastro Realizado com sucesso'
    return render(request, 'cadastro.html', args)
