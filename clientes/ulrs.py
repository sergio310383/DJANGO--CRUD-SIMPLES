from django.urls import path
from .views import list_clientes, create_clientes, update_clientes, delete_clientes

namespace="clientes"

urlpatterns = [
    path('', list_clientes, name='list_clientes'),
    path('create/', create_clientes, name='create_clientes'),
    path('update/<int:id>/', update_clientes,name='update_clientes'),
    path('delete/<int:id>/', delete_clientes, name='delete_clientes'),
]