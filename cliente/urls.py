from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cliente', views.listar_cliente, name='listar_clientes'),
    path('cliente/new/', views.cadastrar_usuario, name='cadastrar_cliente'), 
    path('cliente/editar/<int:id>/', views.editar_cliente, name='editar_cliente'),
    path('clt_carteira/editar/<int:id>/', views.carteira_cliente, name='carteira_cliente'),
    path('page_login', views.page_login, name='page_login'),
    path('autenticar_usuario', views.autenticar_usuario, name='autenticar_usuario'),
     path('logout_usuario', views.logout_usuario, name='logout_usuario'),
]