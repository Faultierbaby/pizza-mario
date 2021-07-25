from django.urls import path
from . import views

urlpatterns = [
    path('', views.startseite, name='startseite'),
    path('index', views.index_kunde, name='index_kunde'),
    path('pizzakreation', views.kreation, name='kreation'),
    path('pizzakreation/erfolgreich', views.kreation_erfolgreich, name='kreation_erfolgreich'),
    path('zutatenliste', views.zutatenliste, name='zutatenliste'),
    path('bestellung', views.bestellung, name='bestellung'),
    path('bestellung/erfolgreich', views.bestellung_erfolgreich, name='bestellung_erfolgreich'),
    path('bestellung/error', views.bestellung_error, name='bestellung_error')
]