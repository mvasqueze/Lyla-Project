from django.shortcuts import render
from django.http import HttpResponse
from .models import Metodo
from django.shortcuts import get_object_or_404
from . import forms
from . import metodos 

# Create your views here.
def home(request):
    searchTerm = request.GET.get('searchMethod')
    if searchTerm:
        metodos = Metodo.objects.filter(title__icontains=searchTerm)
    else:
        metodos = Metodo.objects.all()
    return render(request, 'home.html', {'searchTerm': searchTerm, 'metodos': metodos})

def about(request):
    return HttpResponse('<h1>Welcome to the Jungle, baby (about)<h1>')

def signup(request):
    email = request.GET.get('email')
    return render(request, 'signup.html', {'email':email})

def detail(request, metodo_id):
    metodo=get_object_or_404(Metodo, pk=metodo_id)
    return render(request, 'detail.html',{'metodo': metodo})

def biseccion(request):
    if request.method == 'POST':
        form = forms.BiseccionForm(request.POST)
        if form.is_valid():
            f = form.cleaned_data['f']
            xi = form.cleaned_data['xi']
            xs = form.cleaned_data['xs']
            tol = form.cleaned_data['tol']
            niter = form.cleaned_data['niter']

            # Llamar a la función biseccion con los datos del formulario
            resultados_tabla, resultado_final = metodos.biseccion(f, xi, xs, tol, niter)
            print('AAAA ESTE SÍ ES EL RESULTADO AAAAA')
            print(resultados_tabla)
            print('AAAA ESTE SÍ ES EL RESULTADO AAAAA')
            print(resultado_final)
            # Pasar los resultados a la plantilla para mostrar la tabla
            return render(request, 'biseccion.html', {
                'form': form,
                'resultados_tabla': resultados_tabla,
                'resultado_final': resultado_final
            })
    else:
        form = forms.BiseccionForm()
        print('AAAA ESTE NO ES EL RESULTADO AAAAA')

    return render(request, 'biseccion.html', {'form': form})

def regla_falsa(request):
    if request.method == 'POST':
        form = forms.ReglaFalsaForm(request.POST)
        if form.is_valid():
            f = form.cleaned_data['f']
            xi = form.cleaned_data['xi']
            xs = form.cleaned_data['xs']
            t_error = form.cleaned_data['t_error']
            tol = form.cleaned_data['tol']
            niter = form.cleaned_data['niter']
            print('ENTRA AL IF')
            #regla_falsa(f,t_error,xinf,xsup,tol,niter)
            resultados_tabla, resultado_final = metodos.regla_falsa(f, t_error, xi, xs, tol, niter)
            print('TIPO DE ERROR:')
            print(t_error)
            print(resultados_tabla)
            print('AAAA ESTE SÍ ES EL RESULTADO AAAAA')
            print(resultado_final)
            # Pasar los resultados a la plantilla para mostrar la tabla
            return render(request, 'regla_falsa.html', {
                'form': form,
                'resultados_tabla': resultados_tabla,
                'resultado_final': resultado_final
            })
    else:
        form = forms.ReglaFalsaForm()
        print('AAAA ESTE NO ES EL RESULTADO AAAAA')

    return render(request, 'regla_falsa.html', {'form': form})

def punto_fijo(request):
    if request.method == 'POST':
        form = forms.PuntoFijoForm(request.POST)
        if form.is_valid():
            f = form.cleaned_data['f']
            g = form.cleaned_data['g']
            x0 = form.cleaned_data['x0']
            tol = form.cleaned_data['tol']
            niter = form.cleaned_data['niter']

            #def punto_fijo(f, g, x0, tol, niter):
            resultados_tabla, resultado_final = metodos.punto_fijo(f, g, x0, tol, niter)
            print('AAAA ESTE SÍ ES EL RESULTADO AAAAA')
            print(resultados_tabla)
            print('AAAA ESTE SÍ ES EL RESULTADO AAAAA')
            print(resultado_final)
            # Pasar los resultados a la plantilla para mostrar la tabla
            return render(request, 'punto_fijo.html', {
                'form': form,
                'resultados_tabla': resultados_tabla,
                'resultado_final': resultado_final
            })
    else:
        form = forms.PuntoFijoForm()
        print('AAAA ESTE NO ES EL RESULTADO AAAAA')

    return render(request, 'punto_fijo.html', {'form': form})

#def newton_raphson(f, df, x0, tol, niter):
def newton(request):
    if request.method == 'POST':
        form = forms.NewtonForm(request.POST)
        if form.is_valid():
            f = form.cleaned_data['f']
            df = form.cleaned_data['df']
            x0 = form.cleaned_data['x0']
            tol = form.cleaned_data['tol']
            niter = form.cleaned_data['niter']

            resultados_tabla, resultado_final = metodos.newton_raphson(f, df, x0, tol, niter)
            print('AAAA ESTE SÍ ES EL RESULTADO AAAAA')
            print(resultados_tabla)
            print('AAAA ESTE SÍ ES EL RESULTADO AAAAA')
            print(resultado_final)
            # Pasar los resultados a la plantilla para mostrar la tabla
            return render(request, 'newton.html', {
                'form': form,
                'resultados_tabla': resultados_tabla,
                'resultado_final': resultado_final
            })
    else:
        form = forms.NewtonForm()
        print('AAAA ESTE NO ES EL RESULTADO AAAAA')

    return render(request, 'newton.html', {'form': form})

def secante(request):
    if request.method == 'POST':
        form = forms.SecanteForm(request.POST)
        if form.is_valid():
            f = form.cleaned_data['f']
            x0 = form.cleaned_data['x0']
            x1 = form.cleaned_data['x1']
            tol = form.cleaned_data['tol']
            niter = form.cleaned_data['niter']

            #def secante(x0, x1, f, tol, niter)
            resultados_tabla, resultado_final = metodos.secante(x0, x1, f, tol, niter)
            print('AAAA ESTE SÍ ES EL RESULTADO AAAAA')
            print(resultados_tabla)
            print('AAAA ESTE SÍ ES EL RESULTADO AAAAA')
            print(resultado_final)
            # Pasar los resultados a la plantilla para mostrar la tabla
            return render(request, 'secante.html', {
                'form': form,
                'resultados_tabla': resultados_tabla,
                'resultado_final': resultado_final
            })
    else:
        form = forms.SecanteForm()
        print('AAAA ESTE NO ES EL RESULTADO AAAAA')

    return render(request, 'secante.html', {'form': form})

#multiple_roots(x0, f, df, df2, tol, niter)
def r_multiples(request):
    if request.method == 'POST':
        form = forms.MultipleRootsForm(request.POST)
        if form.is_valid():
            f = form.cleaned_data['f']
            df = form.cleaned_data['df']
            df2 = form.cleaned_data['df2']
            x0 = form.cleaned_data['x0']
            tol = form.cleaned_data['tol']
            niter = form.cleaned_data['niter']

            resultados_tabla, resultado_final = metodos.multiple_roots(x0, f, df, df2, tol, niter)
            print('AAAA ESTE SÍ ES EL RESULTADO AAAAA')
            print(resultados_tabla)
            print('AAAA ESTE SÍ ES EL RESULTADO AAAAA')
            print(resultado_final)
            # Pasar los resultados a la plantilla para mostrar la tabla
            return render(request, 'r_multiples.html', {
                'form': form,
                'resultados_tabla': resultados_tabla,
                'resultado_final': resultado_final
            })
    else:
        form = forms.MultipleRootsForm()
        print('AAAA ESTE NO ES EL RESULTADO AAAAA')

    return render(request, 'r_multiples.html', {'form': form})
