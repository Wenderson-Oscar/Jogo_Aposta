from django.shortcuts import redirect, render, get_object_or_404
from cliente.models import Cliente, Carteira
from cliente.forms import Formulario, Formulario_Carteira
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def logout_usuario(request):
    logout(request)
    return render(request, 'usuarios/page_login.html',{})


def autenticar_usuario(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        cliente = Cliente.objects.all()
        return render(request, 'usuarios/listar_clientes.html', {'clientes':cliente})
    else:
        return render(request, 'usuarios/page_login.html',{})


def page_login(request):
    return render(request, 'usuarios/page_login.html',{})


def carteira_cliente(request, id):
    clt_carteira = get_object_or_404(Carteira, pk=id)
    if request.method == "POST":
        form = Formulario_Carteira(request.POST, request.FILES, instance=clt_carteira)
        if form.is_valid():
            clt_carteira = form.save(commit=False)
            form.save()
            return redirect('editar_cliente', id=clt_carteira.id)
    else:
        form = Formulario_Carteira(instance=clt_carteira)
        return render(request, 'usuarios/carteira_cliente.html', {'form': form})


def editar_cliente(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    if request.method == "POST":
        form = Formulario(request.POST, request.FILES, instance=cliente)
        if form.is_valid():
            cliente = form.save(commit=False)
            form.save()
            return redirect('editar_cliente', id=cliente.id)
    else:
        form = Formulario(instance=cliente)
        return render(request, 'usuarios/form.html', {'form': form})


def cadastrar_usuario(request):
    if request.method == "POST":
        form = Formulario(request.POST, request.FILES)
        if form.is_valid():
            cliente = form.save(commit=False)
            form.save()
            return redirect('editar_cliente', id=cliente.id)
    else:
        form = Formulario()
        return render(request, 'usuarios/form.html', {'form': form})


def home(request):
    clientes = Cliente.objects.all()
    return render(request, 'usuarios/home.html', {'clientes': clientes})


def listar_cliente(request):
    cliente = Cliente.objects.all()
    return render(request, 'usuarios/listar_clientes.html', {'clientes': cliente})
