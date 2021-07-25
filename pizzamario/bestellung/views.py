from django.shortcuts import render, redirect
from .forms import PizzaForm, BestellungForm
from .models import Zutat, Pizza, PizzaZutatnummer

# Create your views here.
def startseite(request):
    return render(request, 'bestellung/startseite.html')

def index_kunde(request):
    return render(request, 'bestellung/index_kunde.html')

def kreation(request):
    if request.method == "POST":
        form = PizzaForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            form.save_m2m()
            return redirect('kreation_erfolgreich')
    else:
        form = PizzaForm()
        return render(request, 'bestellung/kreation.html', {'form': form})

def kreation_erfolgreich(request):
    return render(request, 'bestellung/kreation_erfolgreich.html')

def zutatenliste(request):
    zutaten = Zutat.objects.filter(status=True)
    return render(request, 'bestellung/zutatenliste.html', {'zutaten': zutaten})

def bestellung(request):
    if request.method == "POST":
        form = BestellungForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)

            # Verfuegbarkeit aller verwendeten Zutaten ueberpruefen
            zutatenliste = post.pizzanummer.zutatnummer.all()
            for z in zutatenliste:
                if z.status == False:
                    return redirect('bestellung_error')
            post.save()
            return redirect('bestellung_erfolgreich')
    else:
        form = BestellungForm()
        return render(request, 'bestellung/bestellung.html', {'form': form})

def bestellung_erfolgreich(request):
    return render(request, 'bestellung/bestellung_erfolgreich.html')

def bestellung_error(request):
    return render(request, 'bestellung/bestellung_error.html')