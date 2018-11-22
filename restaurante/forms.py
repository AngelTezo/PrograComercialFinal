from django import forms
from .models import Menu, Plato

class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ('nombre','total')

class PlatoForm(forms.ModelForm):
    class Meta:
        model = Plato
        fields = ('nombre', 'precio')

def __init__(self, *args, **kwargs):
    super(MenuForm, self).__init__(*args, **kwargs)
    self.fields["plato"].widget = forms.widgets.CheckboxSelectMultiple()
    self.fields["plato"].help_text = "Ingrese los platillos de este menu"
    self.fields["plato"].queryset = Plato.objects.all()
