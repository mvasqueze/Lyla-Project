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