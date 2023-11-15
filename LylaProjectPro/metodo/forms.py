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
