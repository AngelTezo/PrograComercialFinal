from django import forms
from .models import Menu, Plato

class PeliculaForm(forms.ModelForm):

    class Meta:
        model = Menu
        fields = ('nombre' )

def __init__ (self, *args, **kwargs):
        super(PeliculaForm, self).__init__(*args, **kwargs)
        self.fields["plato"].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields["plato"].help_text = "Ingrese los Actores que participaron en la película"
        self.fields["plato"].queryset = Plato.objects.all()