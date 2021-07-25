# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Bestellung(models.Model):
    nummer = models.AutoField(primary_key=True)
    pizzanummer = models.ForeignKey('Pizza', models.DO_NOTHING, db_column='pizzanummer', blank=True, null=True)
    kundenmail = models.TextField(null=False)

    class Meta:
        db_table = 'bestellung'
        verbose_name_plural = "Pizzabestellungen"
   
    def __str__(self):
        return f"#{self.nummer}"


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


SIZE_CHOICES = (
    ("klein", "klein"),
    ("normal", "normal"),
    ("groß", "groß"),
)

class Pizza(models.Model):
    nummer = models.AutoField(primary_key=True)
    groesse = models.CharField(max_length=6, blank=True, null=True, choices = SIZE_CHOICES)
    name = models.TextField(blank=True, null=True, max_length=20)
    zutatnummer = models.ManyToManyField('Zutat') 

    class Meta:
        db_table = 'pizza'
        verbose_name_plural = "Pizzakreationen"

    def __str__(self):
        zutaten = ",\n".join([p.name + " (" + p.herkunft + ")" for p in self.zutatnummer.all()])
        gp = 0
        for z in self.zutatnummer.all():
            gp += z.preis
        if(self.groesse == "klein"):
            gp += 2
        if (self.groesse == "normal"):
            gp += 3
        else:
            gp += 4
        return "{} [{}]: {} = {} Münzen".format(self.name, self.groesse, zutaten, gp)


class PizzaZutatnummer(models.Model):
    pizza = models.ForeignKey(Pizza, models.DO_NOTHING)
    zutat = models.ForeignKey('Zutat', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pizza_zutatnummer'
        unique_together = (('pizza', 'zutat'),)


class Vorrat(models.Model):
    zutatnummer = models.OneToOneField('Zutat', models.DO_NOTHING, db_column='zutatnummer', blank=True, null=False, primary_key=True)
    menge = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'vorrat'
        verbose_name_plural = "Vorrat"
    
    def __str__(self):
        return f"{self.menge}g"


class Zulieferer(models.Model):
    name = models.TextField(primary_key=True)
    adresse = models.TextField(blank=True, null=True)
    status = models.BooleanField(blank=True, null=True)

    class Meta:
        db_table = 'zulieferer'
        verbose_name_plural = "Zulieferer"
    
    def __str__(self):
        return f"{self.name}"


class Zutat(models.Model):
    nummer = models.AutoField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    herkunft = models.TextField(blank=True, null=True)
    preis = models.FloatField(blank=True, null=True)
    zulieferername = models.ForeignKey(Zulieferer, models.DO_NOTHING, db_column='zulieferername', blank=True, null=True)
    status = models.BooleanField(default=False)

    class Meta:
        db_table = 'zutat'
        verbose_name_plural = "Zutaten"

    def __str__(self):
        return f"{self.name} ({self.herkunft}) - {self.preis} Münzen"