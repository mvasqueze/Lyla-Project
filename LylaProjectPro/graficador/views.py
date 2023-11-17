from django.shortcuts import render
import matplotlib.pyplot as plt
import numpy as np
import io
import urllib, base64
import math

def graficadorSimple(request):
    imagen_grafico = None
    error = None

    if request.method == 'POST':
        funcion = request.POST.get('funcion')
        print('esta es la función: ')
        print(funcion)
        # Graficar la función
        if funcion:
            try:
                x = np.linspace(-10, 10, 1000) 
                y = np.empty_like(x)
                # Evaluate the expression for each x value
                for i, x_val in enumerate(x):
                    # Use eval with a dictionary to allow math functions within the eval context
                    y[i] = eval(funcion, {'__builtins__': None}, {'x': x_val, 'math': math})
                # Evaluate the function to generate y values
                print('B: ')
                print(y)

                plt.figure(figsize=(8, 6))
                plt.plot(x, y)
                plt.xlabel('x')
                plt.ylabel('f(x)')
                plt.title('Gráfico de la función: ' + funcion)
                plt.grid(True)

                # Convert the plot to an image to display on the page
                buffer = io.BytesIO()
                plt.savefig(buffer, format='png')
                buffer.seek(0)
                imagen_grafico = base64.b64encode(buffer.getvalue()).decode('utf-8')
                plt.close()

            except Exception as e:
                # Handle errors when evaluating the function
                error = f"Error al evaluar la función: {e}"
                print(error)

    return render(request, 'graficadorSimple.html', {'imagen_grafico': imagen_grafico, 'error': error})

def graficador(request, funcion):
    print('esta es la función: ')
    print(funcion)
    
    imagen_grafico = None
    error = None
    
    # Graficar la función
    if funcion:
        try:
            x = np.linspace(-10, 10, 1000) 
            y = np.empty_like(x)
            # Evaluate the expression for each x value
            for i, x_val in enumerate(x):
                # Use eval with a dictionary to allow math functions within the eval context
                y[i] = eval(funcion, {'__builtins__': None}, {'x': x_val, 'math': math})
            # Evaluate the function to generate y values
            print('B: ')
            print(y)

            plt.figure(figsize=(8, 6))
            plt.plot(x, y)
            plt.xlabel('x')
            plt.ylabel('f(x)')
            plt.title('Gráfico de la función: ' + funcion)
            plt.grid(True)

            # Convert the plot to an image to display on the page
            buffer = io.BytesIO()
            plt.savefig(buffer, format='png')
            buffer.seek(0)
            imagen_grafico = base64.b64encode(buffer.getvalue()).decode('utf-8')
            plt.close()

        except Exception as e:
            # Handle errors when evaluating the function
            error = f"Error al evaluar la función: {e}"
            print(error)

    return render(request, 'graficador.html', {'imagen_grafico': imagen_grafico, 'error': error, 'funcion':funcion})