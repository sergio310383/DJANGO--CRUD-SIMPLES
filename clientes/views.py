from django.shortcuts import render, redirect
from .models import Cliente
from .forms import ClienteForm


def list_clientes(request):
    dados = Cliente.objects.all()
    return render(request, 'clientes.html', {'dados': dados})

def create_clientes(request):
    form = ClienteForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_clientes')

    return render(request, 'clientes-form.html', {'form': form})

def update_clientes(request, id):
    dados = Cliente.objects.get(id=id)
    form = ClienteForm(request.POST or None, instance=dados)

    if form.is_valid():
        form.save()
        return redirect('list_clientes')

    return render(request, 'clientes-form.html', {'form': form, 'dados': dados})


def delete_clientes(request, id):
    print(id)
    dados = Cliente.objects.get(id=id)

    if request.method == 'POST':
        dados.delete()
        return redirect('list_clientes')

    return render(request, 'prod-delete-confirm.html', {'dados': dados})
