from django.urls import path
from .views import listarClientes, detalharCliente, cadastrarCliente, deletarCliente

urlpatterns = [
    path('novo/', cadastrarCliente, name='cadastrar_cliente'),
    path('detalhe/<int:id>/', detalharCliente, name='detalhar_cliente'),
    path('deletar/<int:id>/', deletarCliente, name='deletar_cliente'),
    path('lista/', listarClientes, name='listar_clientes'),
]
