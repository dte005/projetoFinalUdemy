from django.shortcuts import render, get_object_or_404, redirect
from .models import Pessoa
from .forms import createPessoaForm
from django.contrib.auth.decorators import login_required

@login_required()
def listarClientes(request):
    query = Pessoa.objects.all()
    return render(request, 'listar_pessoa.html', {'pessoas':query})

@login_required()
def cadastrarCliente(request):
    form = createPessoaForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('listar_clientes')

    return render(request, 'pessoa_formulario.html', {'form':form})

@login_required
def deletarCliente(request, id):
    query = get_object_or_404(Pessoa, pk=id)
    form = createPessoaForm(request.POST or None, request.FILES or None, instance=query)

    if request.method == 'POST':
        query.delete()
        return redirect('listar_clientes')

    return render(request,'deletar_pessoa.html', {'form':form})

@login_required
def detalharCliente(request, id):
    query = get_object_or_404(Pessoa, pk=id)
    form = createPessoaForm(request.POST or None, request.FILES or None, instance=query)
    if form.is_valid():
        form.save()
        return redirect('listar_clientes')

    return render(request, 'pessoa_formulario.html', {'form':form})
