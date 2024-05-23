from django.contrib import admin
from .models import Driver, Vehicle, AccountingRecord

# Register your models here.
# ModelAdmin es una clase que se utiliza para definir la configuración del panel de administración de Django para un modelo
class DriverAdmin(admin.ModelAdmin):
    fields = ['rut', 'name', 'last_name', 'active', 'vehicle','created_at'] # Definir los campos a mostrar en el formulario del administrador, en este caso created_ad solo se mostrará sin poder editarlo.
    readonly_fields = ['created_at'] # Definir los campos de solo lectura
    
class VehicleAdmin(admin.ModelAdmin):
    fields = ['registration_plate', 'brand', 'model', 'year', 'active','created_at']
    readonly_fields = ['created_at']
    
class AccountingRecordAdmin(admin.ModelAdmin):
    fields = ['date_of_purchase', 'price', 'vehicle']
    

admin.site.register(Driver, DriverAdmin)
admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(AccountingRecord, AccountingRecordAdmin)