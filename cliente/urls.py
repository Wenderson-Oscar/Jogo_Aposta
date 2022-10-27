from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cliente', views.listar_cliente, name='listar_clientes'),
    path('cliente/new/', views.cadastrar_usuario, name='cadastrar_cliente'),
    path('cliente/editar/<int:id>/', views.editar_cliente, name='editar_cliente'),  # type: ignore
    path('clt_carteira/editar/<int:id>/', views.carteira_cliente ,name='carteira_cliente'),   # type: ignore
    path('page_login', views.page_login, name='page_login'),
    path('autenticar_usuario', views.autenticar_usuario, name='autenticar_usuario'),
    path('logout_usuario', views.logout_usuario, name='logout_usuario'),
    path('create_user', views.create_user, name='create_user'),
    path('perfil', views.perfil, name='perfil'),
    path('sorteado', views.premiu, name='sorteado'),
    path('bilhete', views.bilhetes, name='bilhete'),
    path('bichos', views.escolhar_bichos, name='escolha_bichos'),
    path('result_bichos', views.premiu_bichos, name='result_bichos'),
]