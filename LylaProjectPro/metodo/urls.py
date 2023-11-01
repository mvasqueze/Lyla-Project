from django.urls import path
from . import views

urlpatterns = [
    path('<int:metodo_id>', views.detail, name='detail'),
]