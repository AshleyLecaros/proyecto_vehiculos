from django.db import models
from django.db.models import PROTECT
from django.utils import timezone

# Create your models here.

class Driver(models.Model):
    rut = models.CharField(max_length=9, primary_key=True)
    name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    active = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now) # almacena la fecha y hora en que se creó el objeto, y si no se proporciona un valor al crearlo, se utilizará la fecha y hora actuales automáticamente.
    # Campo 'vehicle' que establece una relación uno a uno con el modelo 'Vehicle'.
    vehicle = models.OneToOneField(
        "vehicle",
        related_name="driver", # Este parametro define el nombre del campo inverso para acceder al Driver desde el modelo Vehicle, es decir desde el modelo Driver puedo acceder a este campo como vehicle, pero desde el modelo Vehicle podré acceder con el nombre driver.
        null=True,
        blank=True,
        on_delete=models.PROTECT,  # se usa 'PROTECT' para evitar la eliminación del vehiculo si este esta asignado a un conductor.
    )  
    
    
    # devuelve una representación en cadena del objeto, en este caso, devuelve el rut del conductor.
    def __str__(self):
        return self.rut
    
    
    class Meta: 
        verbose_name = "driver" # Nombre singular del modelo en el administrador de Django.
        verbose_name_plural = "drivers" # Nombre plural del modelo en el administrador de Django.
        ordering = ["rut"] # Orden predeterminado de los registros al realizar consultas, ordenado por rut.
        
class Vehicle(models.Model):
    registration_plate = models.CharField(max_length=6, primary_key=True)
    brand = models.CharField(max_length=20, null=False, blank=False)
    model = models.CharField(max_length=20, null=False, blank=False)
    year = models.DateField(null=False, blank=False)
    active = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.registration_plate
    
    class Meta: 
        verbose_name = "vehicle" 
        verbose_name_plural = "vehicles"  
        ordering = ["registration_plate"]
        
class AccountingRecord(models.Model):
    date_of_purchase = models.DateField(null=False, blank=False)
    price = models.FloatField(null=False, blank=False)
    vehicle = models.OneToOneField(
        "vehicle", related_name="accouting", on_delete=PROTECT
    ) # impide la eliminación del Vehicle si existe una referencia en AccountingRecord.
    
    def __str__(self):
        return self.vehicle.registration_plate
    

    class Meta: 
        verbose_name = "Accounting Record"  
        verbose_name_plural = "Accounting Records"
        ordering = ["date_of_purchase"] 
    
    
    
    
    
    
