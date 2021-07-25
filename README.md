# pizza-mario


## Hintergrund

Das Projekt ist im Rahmen der Vorlesung *Advanced Management of Data* im Wintersemester 2020/21 an der TU Chemnitz entstanden. Die Aufgabenstellung umfasste die Konzeption und Initialisierung einer PostgreSQL-Datenbank zum Szenario "Pizzakreationen" und die Realisierung eines dazugehörigen Front-Ends für die Bestellung und Verwaltung der Pizzen. Das Front-End wurde mithilfe des Webframeworks "Django" (https://www.djangoproject.com/download/) realisiert.


## Aufbau des Projektordners 

In dem vorliegenden Projektordner befinden sich folgende Dateien:

1. 'UML.png': UML-Diagramm / Konzeption der relationalen Datenbank

2. 'DB_Skript.txt': Initialisierungsskript der PostgreSQL-Datenbank (Tabellen, Testdaten, Trigger)

3. Unterverzeichnis 'pizzamario': Django-Projektverzeichnis 


## Django-Installation 

Um den Pizza-Manager zu starten, sind folgende Installations- und Konfigurationsschritte sind notwendig:

1. Python 3 (https://www.python.org/downloads/)

2. Virtuelle Umgebung einrichten und aktivieren
```
$ mkdir djangoprojects
$ cd djangoprojects
$ python3 -m venv pizzaenv
$ source pizzaenv/bin/activate
```

3. Pip
```
(pizzaenv) ~$ python -m pip install --upgrade pip
```

4. Django
```
(pizzaenv) ~$ python -m pip install Django
```


## Datenbank 

### Variante 1: SQLite
Standardmäßig enthält die Python-Installation eine Python-SQL-Bibliothek namens sqlite3, die zur Interaktion mit einer SQLite-Datenbank verwenden werden kann.
In der Datei 'pizzamario/settings.py' ist bei Projektstart bereits eine default-Konfiguration zu einer SQLite-Datenbank hinterlegt, die von Django lokal angelegt wird:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```
Um die SQLite-Datenbank mit Tabellen zu füllen, muss auf Grundlage der Django-Models in `pizzamario/bestellung/models.py` eine Migration ausgeführt werden:

```
(pizzaenv) ~$ python manage.py makemigrations bestellung
(pizzaenv) ~$ python manage.py migrate bestellung
```

### Variante 2: PostgreSQL
Idealerweise wird hier jedoch eine PostgreSQL-Datenbank gewählt, weil im vorliegenden Projektordner bereits ein Initialisierungskript mit Tabellen, Testdaten und Trigger vorliegt. Eine Migration der Django-Models ist dann nicht mehr notwendig. In 'pizzamario/settings.py' müssen nur noch die Authentifizierungs-Felder (`NAME, USER, PASSWORD, HOST, PORT`) der zuvor initialisierten Datenbank angepasst werden:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'name-of-your-database',
        'USER': 'user-name',
        'PASSWORD': 'password',
        'HOST': 'host',
        'PORT': '1234',
    }
}
```
## Pizza-Manager starten 

1. In das Projektverzeichnis navigieren
```
(pizzaenv) ~$ cd /.../pizzamario
```
2. Testserver starten
```
(pizzaenv) ~$ python manage.py runserver
```
[alternativ: `(pizzaenv) ~$ python manage.py runserver 0:8000]`

3. Browser öffnen: http://127.0.0.1:8000

4. Pizza kreieren & Bestellung abschicken ;-)


## Administrationsoberfläche des Pizzabäckers 

In der Pizzabäcker-Ansicht (http://127.0.0.1:8000/admin) werden die Login-Daten eines Super-Users benötigt.

Ein Superuser wird wie folgt erstellt:
```
(pizzaenv) ~$ python manage.py createsuperuser
```
Im Django-Admin können schließlich die Pizzen, Bestellungen, Zutaten und Zulieferer verwaltet werden.


## Bildquellen 

pizzamario/pizzamario/bestellung/static/img/background.png: 
https://images6.alphacoders.com/860/860645.png

pizzamario/pizzamario/bestellung/static/img/logo.jpg: 
https://www.pinterest.es/pin/676102962797570346/
