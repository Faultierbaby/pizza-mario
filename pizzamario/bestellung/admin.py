from django.contrib import admin, messages
from .models import Bestellung, Zutat, Vorrat, Zulieferer, Pizza
from django.db.models import Sum

admin.site.site_header = 'Pizza-Manager'
admin.site.index_title  = 'Willkommen bei Pizza Mario!'

# Register your models here.

@admin.register(Bestellung)
class BestellungAdmin(admin.ModelAdmin):
    list_display = ("bestellnummer", "kunde", "pizzakreation")

    def bestellnummer(self, obj):
        return obj.nummer

    def pizzakreation(self, obj):
        return obj.pizzanummer
    
    def kunde(self, obj):
        return obj.kundenmail
    
  
@admin.register(Zutat)
class ZutatAdmin(admin.ModelAdmin):
    list_display = ("name", "herkunft", "zulieferername", "preis", "vorrat", "status")
    list_filter = ("status", "zulieferername__name", "herkunft", "preis")
    actions = ["set_status_true", "set_status_false",]
    list_editable = ("preis",)
    search_fields = ["name", "herkunft", "zulieferername__name"]

    def set_status_true(self, request, queryset):
        updated = queryset.update(status=True)
        self.message_user(request, '{} Zutat(en) als verfügbar markiert.'.format(updated))
    set_status_true.short_description = "Ausgewählte Zutat(en) als verfügbar markieren"

    def set_status_false(self, request, queryset):
        updated = queryset.update(status=False)
        self.message_user(request, '{} Zutat(en) als NICHT verfügbar markiert.'.format(updated))
    set_status_false.short_description = "Ausgewählte Zutat(en) als NICHT verfügbar markieren"
        

@admin.register(Zulieferer)
class ZuliefererAdmin(admin.ModelAdmin):
    list_display = ("name", "adresse", "status")
    list_filter = ("status",)
    actions = ["set_status_true", "set_status_false",]

    def set_status_true(self, request, queryset):
        updated = queryset.update(status=True)
        self.message_user(request, '{} Zulieferer als verfügbar markiert.'.format(updated))
    set_status_true.short_description = "Ausgewählte Zulieferer als verfügbar markieren"

    def set_status_false(self, request, queryset):
        updated = queryset.update(status=False)
        self.message_user(request, '{} Zulieferer als NICHT verfügbar markiert.'.format(updated))
    set_status_false.short_description = "Ausgewählte Zulieferer als NICHT verfügbar markieren"


@admin.register(Vorrat)
class VorratAdmin(admin.ModelAdmin):
    list_display = ("name", "herkunft", "zulieferer", "lieferstatus", "menge_g")
    actions = ["add_1", "add_5", "add_10", "add_50", "add_100", "add_500", "add_1000"]
    search_fields = ["zutatnummer__herkunft", "zutatnummer__name"]

    def name(self, obj):
        return obj.zutatnummer.name

    def herkunft(self, obj):
        return obj.zutatnummer.herkunft
    
    def zulieferer(self, obj):
        return obj.zutatnummer.zulieferername
 
    def lieferstatus(self, obj):
        if obj.zutatnummer.zulieferername.status == True:
            return "✔"
    
    def menge_g(self, obj):
        return str(obj.menge) + "g"

    def add_1(self, request, queryset):
        for item in queryset:
            if item.zutatnummer.zulieferername.status == True:
                item.menge = item.menge+1
                item.save()
            else: 
                messages.error(request, "Zutat '{}' kann von {} momentan leider nicht geliefert werden. Bitte wähle einen anderen Zulieferer!".format(item.zutatnummer.name, item.zutatnummer.zulieferername))
    add_1.short_description = "+ 1g"

    def add_5(self, request, queryset):
        for item in queryset:
            if item.zutatnummer.zulieferername.status == True:
                item.menge = item.menge+5
                item.save()
            else: 
                messages.error(request, "Zutat '{}' kann von {} momentan leider nicht geliefert werden. Bitte wähle einen anderen Zulieferer!".format(item.zutatnummer.name, item.zutatnummer.zulieferername))
    add_5.short_description = "+ 5g"

    def add_10(self, request, queryset):
        for item in queryset:
            if item.zutatnummer.zulieferername.status == True:
                item.menge = item.menge+10
                item.save()
            else: 
                messages.error(request, "Zutat '{}' kann von {} momentan leider nicht geliefert werden. Bitte wähle einen anderen Zulieferer!".format(item.zutatnummer.name, item.zutatnummer.zulieferername))
    add_10.short_description = "+ 10g"

    def add_50(self, request, queryset):
        for item in queryset:
            if item.zutatnummer.zulieferername.status == True:
                item.menge = item.menge+50
                item.save()
            else: 
                messages.error(request, "Zutat '{}' kann von {} momentan leider nicht geliefert werden. Bitte wähle einen anderen Zulieferer!".format(item.zutatnummer.name, item.zutatnummer.zulieferername))
    add_50.short_description = "+ 50g"

    def add_100(self, request, queryset):
        for item in queryset:
            if item.zutatnummer.zulieferername.status == True:
                item.menge = item.menge+100
                item.save()
            else: 
                messages.error(request, "Zutat '{}' kann von {} momentan leider nicht geliefert werden. Bitte wähle einen anderen Zulieferer!".format(item.zutatnummer.name, item.zutatnummer.zulieferername))
    add_100.short_description = "+ 100g"

    def add_500(self, request, queryset):
            for item in queryset:
                if item.zutatnummer.zulieferername.status == True:
                    item.menge = item.menge+500
                    item.save()
                else: 
                    messages.error(request, "Zutat '{}' kann von {} momentan leider nicht geliefert werden. Bitte wähle einen anderen Zulieferer!".format(item.zutatnummer.name, item.zutatnummer.zulieferername))
    add_500.short_description = "+ 500g"

    def add_1000(self, request, queryset):
            for item in queryset:
                if item.zutatnummer.zulieferername.status == True:
                    item.menge = item.menge+1000
                    item.save()
                else: 
                    messages.error(request, "Zutat '{}' kann von {} momentan leider nicht geliefert werden. Bitte wähle einen anderen Zulieferer!".format(item.zutatnummer.name, item.zutatnummer.zulieferername))
    add_1000.short_description = "+ 1000g"

@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    list_display = ("name", "zutaten")

    def zutaten(self, obj):
        return "\n".join([p.name for p in obj.zutatnummer.all()])
