from django.urls import path
from . import views

urlpatterns = [
    path('<int:metodo_id>', views.detail, name='detail'),
    path('biseccion', views.biseccion, name='biseccion'),
    path('regla_falsa', views.regla_falsa, name='regla_falsa'),
    path('punto_fijo', views.punto_fijo, name='punto_fijo'),
    path('newton', views.newton, name='newton'),
    path('secante', views.secante, name='secante'),
    path('r_multiples', views.r_multiples, name='r_multiples'),
    path('jacobi', views.jacobi, name='jacobi'),
    path('seidel', views.seidel, name='seidel'),
    path('sor', views.sor, name='sor'),
    #path('vander', views.vander, name='vander'),
    #path('newton_int', views.newton_int, name='newton_int'),
    #path('lagrange', views.lagrange, name='lagrange'),
    #path('spline_l', views.spline_l, name='spline_l'),
    #path('spline_c', views.spline_c, name='spline_c'),
]