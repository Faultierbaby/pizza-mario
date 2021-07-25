from django import forms
from .models import Pizza, Zutat, Bestellung, PizzaZutatnummer
from django.forms import TextInput, CheckboxSelectMultiple
from django.db.models import Prefetch

class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ('name', 'groesse', 'zutatnummer')
        labels = {
            'zutatnummer': ('Zutatenauswahl')
        }
        widgets = {
            'name' : TextInput(attrs={'class': 'input-mini'}),
        }

    def __init__ (self, *args, **kwargs):
        super(PizzaForm, self).__init__(*args, **kwargs)
        self.fields["name"].help_text = "Gib deiner Pizza-Kreation einen Namen"
        self.fields["groesse"].help_text = "klein = 18cm (+ 2 Münzen) / normal = 24cm (+ 3 Münzen) / gross = 30cm (+ 4 Münzen)"
        self.fields["zutatnummer"].queryset = Zutat.objects.filter(status=True)

class BestellungForm(forms.ModelForm):
    class Meta:
        model = Bestellung
        fields = ('kundenmail','pizzanummer',)
        labels = {
            'pizzanummer': ('Mario backt für dich:'),
            'kundenmail': ('Deine E-Mail-Adresse:')
        }
        widgets = {
            'kundenmail' : TextInput(attrs={'class': 'input-mini'}),
        }


