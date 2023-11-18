from django.urls import path
from . import views

urlpatterns = [
    path('<int:metodo_id>', views.detail, name='detail'),
    path('biseccion', views.biseccion, name='biseccion'),
    path('regla_falsa', views.regla_falsa, name='regla_falsa'),
    path('punto_fijo', views.punto_fijo, name='punto_fijo'),
]