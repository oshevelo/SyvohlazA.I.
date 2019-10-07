class Vehicle(object):
    
    def __init__(self, doors, tires, color, fuelType, vehicleType):
        self.doors = doors
        self.tires = tires
        self.color = color
        self.fuelType = fuelType
        self.vehicleType = vehicleType

    def door(self, isopen=False):
        if isopen:
            return 'Open'
        else:
            return 'Close'
        
    def fuel(self, isfuel=True):
        if isfuel:
            return 'Full Fuel'
        else:
            return 'No Fuel'
        
        
class Car(Vehicle):
    isopen = True
    isfuel = True
    
    def set(self, doors, tires, color, fuelType, vehicleType):
        self.doors = doors
        self.tires = tires
        self.color = color
        self.fuelType = fuelType
        self.vehicleType = vehicleType
    
    def brake(self):
        return 'I`m stop a %s %s' % (self.color, self.vehicleType)
        
    def openCloseDoor(self):
        if not self.isopen:
            return 'Close Door'
        else:
            return 'Open Door'
        
    def noFullFuel(self):
        if not self.isfuel:
            return 'No Fuel'
        else:
            return 'Full Fuel'
        
        
class Truck(Vehicle):
    isopen = False
    isfuel = False
    
    def set(self, doors, tires, color, fuelType, vehicleType, hindcarriage):
        self.doors = doors
        self.tires = tires
        self.color = color
        self.fuelType = fuelType
        self.vehicleType = vehicleType
        self.hindcarriage = hindcarriage

    def openCloseDoor(self):
        if not self.isopen:
            return 'Close Door'
        else:
            return 'Open Door'

    def noFullFuel(self):
        if not self.isfuel:
            return 'No Fuel'
        else:
            return 'Full Fuel'
        
    def drive(self):
        return 'I`m driving a %s %s' % (self.color, self.vehicleType)


car = Car(5, 4, 'red', 'benzine', 'car')
print(car.doors, car.tires, car.color, car.fuelType, car.vehicleType)

truck = Truck(2, 6, 'blue', 'diesel', 'truck')
print(truck.doors, truck.tires, truck.color, truck.fuelType, truck.vehicleType)

print(car.brake())
print(truck.drive())

print('Car: ', car.fuel())
print('Truck: ', truck.fuel())

car.isfuel = False
print('Car: ', car.noFullFuel())
truck.isfuel = True
print('Truck: ', truck.noFullFuel())

car.isopen = True
print('Car:', car.door())
truck.isopen = False
print('Truck:', truck.door())

print('Car:', car.openCloseDoor())
print('Truck: ', truck.openCloseDoor())

car.set(5, 4, 'red', 'benzine', 'car')
print('Doors:', car.doors, ', tires:', car.tires, ', color:', car.color, ', type fuel:', car.fuelType,
      ', type vehicle:', car.vehicleType)

truck.set(2, 6, 'black', 'diesel', 'truck', True)
print('Doors:', truck.doors, ', tires:', truck.tires, ', color:', truck.color, ', type fuel:', truck.fuelType,
      ', type vehicle:', truck.vehicleType, ', hindcarriage:', truck.hindcarriage)


