from django import forms

class BiseccionForm(forms.Form):
    f = forms.CharField(label='Función f(x)')
    xi = forms.FloatField(label='Valor inicial xi')
    xs = forms.FloatField(label='Valor inicial xs')
    tol = forms.FloatField(label='Tolerancia')
    niter = forms.IntegerField(label='Número de iteraciones')

    def clean(self):
        cleaned_data = super().clean()
        xi = cleaned_data.get('xi')
        xs = cleaned_data.get('xs')
        tol = cleaned_data.get('tol')
        niter = cleaned_data.get('niter')

        if xi >= xs:
            raise forms.ValidationError('El valor inicial xi debe ser menor que xs')

        if tol <= 0:
            raise forms.ValidationError('La tolerancia debe ser mayor que cero')

        if niter <= 0:
            raise forms.ValidationError('El número de iteraciones debe ser mayor que cero')

        # Aquí podrías realizar otras validaciones si es necesario

        return cleaned_data
    
class ReglaFalsaForm(forms.Form):
    OPCIONES_ERROR = [
        ('1', 'Cifras significativas'),
        ('2', 'Decimales correctos'),
    ]

    f = forms.CharField(label='Función f(x)')
    xi = forms.FloatField(label='Valor inicial xi')
    xs = forms.FloatField(label='Valor inicial xs')
    t_error = forms.ChoiceField(choices=OPCIONES_ERROR, label='Tipo de Error')
    tol = forms.FloatField(label='Tolerancia')
    niter = forms.IntegerField(label='Número de iteraciones')

    def clean(self):
        cleaned_data = super().clean()
        xi = cleaned_data.get('xi')
        xs = cleaned_data.get('xs')
        tol = cleaned_data.get('tol')
        t_error = cleaned_data.get('t_error')
        niter = cleaned_data.get('niter')

        if xi >= xs:
            raise forms.ValidationError('El valor inicial xi debe ser menor que xs')

        if tol <= 0:
            raise forms.ValidationError('La tolerancia debe ser mayor que cero')

        if niter <= 0:
            raise forms.ValidationError('El número de iteraciones debe ser mayor que cero')

        # Aquí podrías realizar otras validaciones si es necesario

        return cleaned_data

#def punto_fijo(f, g, x0, tol, niter):
class PuntoFijoForm(forms.Form):
    f = forms.CharField(label='Función f(x)')
    g = forms.CharField(label='Función g(x)')
    x0 = forms.FloatField(label='Valor inicial x0')
    tol = forms.FloatField(label='Tolerancia')
    niter = forms.IntegerField(label='Número de iteraciones')

    def clean(self):
        cleaned_data = super().clean()
        x0 = cleaned_data.get('x0')
        tol = cleaned_data.get('tol')
        niter = cleaned_data.get('niter')

        if tol <= 0:
            raise forms.ValidationError('La tolerancia debe ser mayor que cero')

        if niter <= 0:
            raise forms.ValidationError('El número de iteraciones debe ser mayor que cero')

        # Aquí podrías realizar otras validaciones si es necesario

        return cleaned_data
    
#def newton_raphson(f, df, x0, tol, niter):
class NewtonForm(forms.Form):
    f = forms.CharField(label='Función f(x)')
    df = forms.CharField(label='Derivada de f(x)')
    x0 = forms.FloatField(label='Valor inicial x0')
    tol = forms.FloatField(label='Tolerancia')
    niter = forms.IntegerField(label='Número de iteraciones')

    def clean(self):
        cleaned_data = super().clean()
        x0 = cleaned_data.get('x0')
        tol = cleaned_data.get('tol')
        niter = cleaned_data.get('niter')

        if tol <= 0:
            raise forms.ValidationError('La tolerancia debe ser mayor que cero')

        if niter <= 0:
            raise forms.ValidationError('El número de iteraciones debe ser mayor que cero')

        # Aquí podrías realizar otras validaciones si es necesario

        return cleaned_data
    
#def secante(x0, x1, f, tol, niter)
class SecanteForm(forms.Form):
    f = forms.CharField(label='Función f(x)')
    x0 = forms.FloatField(label='Valor inicial x0')
    x1 = forms.FloatField(label='Valor x1')
    tol = forms.FloatField(label='Tolerancia')
    niter = forms.IntegerField(label='Número de iteraciones')

    def clean(self):
        cleaned_data = super().clean()
        x0 = cleaned_data.get('x0')
        x1 = cleaned_data.get('x1')
        tol = cleaned_data.get('tol')
        niter = cleaned_data.get('niter')

        if x0 >= x1:
            raise forms.ValidationError('El valor inicial x0 debe ser menor que x1')
        
        if tol <= 0:
            raise forms.ValidationError('La tolerancia debe ser mayor que cero')

        if niter <= 0:
            raise forms.ValidationError('El número de iteraciones debe ser mayor que cero')

        # Aquí podrías realizar otras validaciones si es necesario

        return cleaned_data

#multiple_roots(x0, f, df, df2, tol, niter)
class MultipleRootsForm(forms.Form):
    f = forms.CharField(label='Función f(x)')
    df = forms.CharField(label='Derivada de f(x)')
    df2 = forms.CharField(label='Segunda derivada de f(x)')
    x0 = forms.FloatField(label='Valor inicial x0')
    tol = forms.FloatField(label='Tolerancia')
    niter = forms.IntegerField(label='Número de iteraciones')

    def clean(self):
        cleaned_data = super().clean()
        x0 = cleaned_data.get('x0')
        tol = cleaned_data.get('tol')
        niter = cleaned_data.get('niter')

        if tol <= 0:
            raise forms.ValidationError('La tolerancia debe ser mayor que cero')

        if niter <= 0:
            raise forms.ValidationError('El número de iteraciones debe ser mayor que cero')

        # Aquí podrías realizar otras validaciones si es necesario

        return cleaned_data
