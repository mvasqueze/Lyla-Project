from django.urls import path
from . import views

urlpatterns = [
    path('', views.graficadorSimple, name='graficadorSimple'),
    path('<path:funcion>', views.graficador, name='graficador'),
]