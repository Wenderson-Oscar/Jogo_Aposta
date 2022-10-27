from array import array
from this import s
from django.shortcuts import redirect, render, get_object_or_404
from cliente.models import Cliente, Carteira, MegaSena, JogoBicho
from cliente.forms import Formulario, Formulario_Carteira, UserCreateForm, EscolhaBicho
from django.contrib.auth import authenticate, login, logout
from random import sample
from datetime import date
# Create your views here.

def premiu_bichos(request):
    """Lógica do bicho"""
    sort = sample(range(0, 100), 2)
    sort.reverse()
    result = []
    escolhar_bichos(request)
    for x in sort:
        for y in select_bichos:
            if str(x) in y:
                result.append(x)
    return render(request, 'usuarios/result_bichos.html', {'sorteado': sort,'bilhetes': select_bichos, 'resultado': result})


def escolhar_bichos(request):
    global select_bichos
    if request.method == "POST":
        form = EscolhaBicho(request.POST)
        select_bichos = request.POST.getlist('bichos', None)
        insert = JogoBicho.objects.create(bichos=select_bichos, data=date.today())
        insert.save()
        return redirect('result_bichos')
    else:
        form = EscolhaBicho()
    return render(request, 'usuarios/form_bichos.html', {'form': form})


def premiu(request):
    """sorteado: lógica da loteria 
    bd: salvando no banco
    resultado: comparando as listar"""
    sorteado = sample(range(1, 61), 6)
    bd = MegaSena(sorteio=str(sorteado), data=date.today())
    bd.save()
    if request.method == "POST":
        bilhetes(request)
        resultado = set(map(str, sorteado)) & set(fusao)
    return render(request, 'usuarios/loteria.html', {'sorteado': sorteado, 'bilhetes': fusao, 'resultado': resultado})


def bilhetes(request):
    global fusao
    if request.method == "POST":
        bilhete0 = request.POST.get('number', None)
        bilhete1 = request.POST.get('number1', None)
        bilhete2 = request.POST.get('number2', None)
        bilhete3 = request.POST.get('number3', None)
        bilhete4 = request.POST.get('number4', None)
        bilhete5 = request.POST.get('number5', None)
        fusao = [bilhete0, bilhete1, bilhete2, bilhete3, bilhete4, bilhete5]
    return render(request, 'usuarios/bilhete.html')


def create_user(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('cadastrar_cliente')
    else:
        form = UserCreateForm()
    return render(request, 'usuarios/form.html',{'form': form})


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
        return render(request, 'usuarios/home.html', {'clientes':cliente})
    else:
        return render(request, 'usuarios/page_login.html',{})


def page_login(request):
    return render(request, 'usuarios/page_login.html',{})


def carteira_cliente(request, id):
    clt_carteira = get_object_or_404(Carteira, pk=id)
    if request.method == "POST":
        form = Formulario_Carteira(request.POST, request.FILES ,instance=clt_carteira)
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
        form = Formulario(request.POST)
        if form.is_valid():
            cliente = form.save(commit=False)
            cliente.user=request.user
            cliente.save()
            form.save()
            return redirect('editar_cliente', id=cliente.id)
    else:                                                                                                                                                                                                                                                                                     
        form = Formulario()
    return render(request, 'usuarios/form.html', {'form': form})


def perfil(request):
    try:
        cliente = Cliente.objects.get(user=request.user)
    except Cliente.DoesNotExist:
        return redirect('cadastrar_cliente')
    return render(request, 'usuarios/detalhar_cliente.html', {'cliente': cliente})


def home(request):
    clientes = Cliente.objects.all()
    return render(request, 'usuarios/home.html', {'clientes': clientes})


def listar_cliente(request):
    cliente = Cliente.objects.all()
    return render(request, 'usuarios/listar_clientes.html', {'cliente': cliente})
