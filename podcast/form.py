from django import forms

from .models import Podcasting, Podcaster



class PodcastingForm(forms.ModelForm):
#todos los campos de Pelicula
    class Meta:
        model = Podcasting
        fields = ('nombre', 'descripcion', 'enlace', 'podcaster')


def __init__ (self, *args, **kwargs):
        super(PodcastingForm, self).__init__(*args, **kwargs)

#En este caso vamos a usar el widget checkbox multiseleccionable.

        self.fields["podcaster"].widget = forms.widgets.CheckboxSelectMultiple()

#Podemos usar un texto de ayuda en el widget

       #self.fields["podcaster"].help_text = "Ingrese los podcasters que participaron en el podcast"

#En este caso le indicamos que nos muestre todos los actores, pero aquí podríamos filtrar datos si fuera necesario

        self.fields["podcaster"].queryset = Podcaster.objects.all()
