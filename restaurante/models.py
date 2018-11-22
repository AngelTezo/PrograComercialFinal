from django.db import models
from django.contrib import admin


class Menu(models.Model):
    nombre =  models.CharField(max_length=30)
    
    def __str__(self):
        return self.nombre


class Plato(models.Model):
    nombre = models.CharField(max_length=60)
    precio = models.IntegerField()

    def __str__(self):
        return self.nombre


#Taba M:M donde se guarda el menu y el plato 
class Carta(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    plato = models.ForeignKey(Plato, on_delete=models.CASCADE)

class Empleado(models.Model):
    nombre = models.CharField(max_length=30,default='')
    puesto = models.CharField(max_length=30,default='')
    
    def __str__(self):
        return self.nombre


class Cliente(models.Model):
    nombre = models.CharField(max_length=60)
    NIT = models.CharField(max_length=60)

    def __str__(self):
        return self.nombre

#Tabla de muchos a muchos de venta asi se sabra que empleado vendio a un cliente 
#y el menu que le vendio
class Venta(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)

class CartaInLine(admin.TabularInline):
    model = Carta

    extra = 1

class PlatoAdmin(admin.ModelAdmin):
    inlines = (CartaInLine,)

class MenuAdmin(admin.ModelAdmin):
    inlines = (CartaInLine,)

class VentaInLine(admin.TabularInline):
    model = Venta

    extra = 1

class ClienteAdmin(admin.ModelAdmin):
    inlines = (VentaInLine,)

class EmpleadoAdmin(admin.ModelAdmin):
    inlines = (VentaInLine,)    
