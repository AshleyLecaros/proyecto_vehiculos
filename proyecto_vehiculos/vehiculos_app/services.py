from vehiculos_app.models import Vehicle, Driver, AccountingRecord

# Función para agregar vehiculo
def create_vehicle(registration_plate, brand, model, year, active):
    vehicle = Vehicle(
        registration_plate = registration_plate,
        brand = brand,
        model = model,
        year = year,
        active = active,
    )
    vehicle.save()
    return vehicle

# Función para crear chofer
def create_driver(rut, name, last_name, active):
    driver = Driver(rut=rut, name=name, last_name=last_name, active=active)
    driver.save()
    return driver

# Función para crear registro contable
def create_accounting_record(vehicle, date_of_purchase, price):
    accounting_record = AccountingRecord(vehicle=vehicle, date_of_purchase=date_of_purchase, price=price)
    accounting_record.save()
    return accounting_record

# Función para deshabilitar chofer
def disable_driver(driver):
    driver.active = False
    driver.save()
    return driver

# Función para deshabilitar vehículo
def disable_vehicle(vehicle):
    vehicle.active = False
    vehicle.save()
    return vehicle

# Función para habilitar chofer
def enable_driver(driver):
    driver.active = True
    driver.save()
    return driver

# Función para habilitar vehículo
def enable_vehicle(vehicle):
    vehicle.active = True
    vehicle.save()
    return vehicle

# Función para obtener vehículo
def get_vehicle(registration_plate):
    return Vehicle.objects.get(registration_plate=registration_plate)

# Función para obtener chofer
def get_driver(rut):
    return Driver.objects.get(rut=rut)

# Función para asignar chofer a vehículo
def asignar_driver_to_vehicle(driver, vehicle):
    vehicle.driver = driver
    vehicle.save()
    driver.save()

# Función para imprimir    
def assign_driver_to_vehicle():
    vehicles = Vehicle.objects.all() # Obtener todos los objetos del modelo Vehicle
    for v in vehicles: # itera sobre cada objeto (v) de Vehicle en la lista vehicles. Si el vehículo tiene un conductor asociado, imprimir los detalles del conductor
        print(
            f"Vehicle:{v.registration_plate}/{v.brand}/{v.model}/" + f"{v.year}/active:{v.active}"
        )
        if hasattr(v, "driver"): # Verificar si el vehículo 'v' tiene un atributo `driver`.
            print(
                f"\tDriver[{v.driver.rut}]:{v.driver.name}" + f"{v.driver.last_name}/active:{v.driver.active}" # \t es una tabulacion, para mejorar la lejibilidad de la impresión.
            )
        if hasattr(v,"accouting"): # Verificar si el vehículo 'v' tiene un atributo 'accouting'
            print(
                f"\taccouting:[{v.accouting.id}]:date_of:purchase:" + f"{v.accouting.date_of_purchase}/price:{v.accouting.price}"
            )
    






    

