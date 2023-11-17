from django.urls import path
from . import views

urlpatterns = [
    path('', views.graficadorSimple, name='graficador'),
    path('<path:funcion>', views.graficador, name='graficador'),
]