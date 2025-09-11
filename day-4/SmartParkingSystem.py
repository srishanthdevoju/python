from abc import ABC, abstractmethod

# ----- Vehicle Classes -----
class Vehicle(ABC):
    def __init__(self, license_plate, owner_name):
        self.__license_plate = license_plate
        self.__owner_name = owner_name

    def get_license_plate(self):
        return self.__license_plate

    def set_license_plate(self, license_plate):
        self.__license_plate = license_plate
    
    def get_owner_name(self):
        return self.__owner_name

    def set_owner_name(self, owner_name):
        self.__owner_name = owner_name

    @abstractmethod
    def display(self):
        pass
    
    @abstractmethod
    def calculate_parking_fee(self, hours):
        pass

class Bike(Vehicle):
    def __init__(self, license_plate, owner_name, helmet_required):
        super().__init__(license_plate, owner_name)
        self.helmet_required = helmet_required

    def display(self):
        print(f"Bike - License: {self.get_license_plate()}, Owner: {self.get_owner_name()}, Helmet Required: {self.helmet_required}")

    def calculate_parking_fee(self, hours):
        return 20 * hours

class Car(Vehicle):
    def __init__(self, license_plate, owner_name, seats):
        super().__init__(license_plate, owner_name)
        self.seats = seats

    def display(self):
        print(f"Car - License: {self.get_license_plate()}, Owner: {self.get_owner_name()}, Seats: {self.seats}")

    def calculate_parking_fee(self, hours):
        return 50 * hours

class SUV(Vehicle):
    def __init__(self, license_plate, owner_name, four_wheel_drive):
        super().__init__(license_plate, owner_name)
        self.four_wheel_drive = four_wheel_drive

    def display(self):
        print(f"SUV - License: {self.get_license_plate()}, Owner: {self.get_owner_name()}, 4WD: {self.four_wheel_drive}")

    def calculate_parking_fee(self, hours):
        return 70 * hours

class Truck(Vehicle):
    def __init__(self, license_plate, owner_name, max_load_capacity):
        super().__init__(license_plate, owner_name)
        self.max_load_capacity = max_load_capacity

    def display(self):
        print(f"Truck - License: {self.get_license_plate()}, Owner: {self.get_owner_name()}, Max Load: {self.max_load_capacity} tons")

    def calculate_parking_fee(self, hours):
        return 100 * hours

# ----- ParkingSpot Class -----
class ParkingSpot:
    def __init__(self, spot_id, size):
        self.spot_id = spot_id
        self.size = size  # 'S', 'M', 'L', 'XL'
        self.__vehicle = None
    
    def get_vehicle(self):
        return self.__vehicle
    
    def is_occupied(self):
        return self.__vehicle is not None
    
    def assign_vehicle(self, vehicle):
        if self.is_occupied():
            print(f"Spot {self.spot_id} already occupied.")
            return False
        
        if self._fits_vehicle(vehicle):
            self.__vehicle = vehicle
            print(f"Vehicle {vehicle.get_license_plate()} assigned to spot {self.spot_id}")
            return True
        else:
            print(f"Vehicle {vehicle.get_license_plate()} does not fit spot size {self.size}")
            return False
    
    def remove_vehicle(self):
        if self.is_occupied():
            v = self.__vehicle
            self.__vehicle = None
            print(f"Vehicle {v.get_license_plate()} removed from spot {self.spot_id}")
            return v
        else:
            print(f"Spot {self.spot_id} is already empty")
            return None
    
    def _fits_vehicle(self, vehicle):
        size_map = {
            'Bike': ['S', 'M', 'L', 'XL'],
            'Car': ['M', 'L', 'XL'],
            'SUV': ['L', 'XL'],
            'Truck': ['XL']
        }
        vehicle_type = type(vehicle).__name__
        allowed_sizes = size_map.get(vehicle_type, [])
        return self.size in allowed_sizes
    
    def status(self):
        status_str = f"Occupied by {self.__vehicle.get_license_plate()}" if self.is_occupied() else "Available"
        print(f"Spot {self.spot_id} [{self.size}]: {status_str}")

# ----- ParkingLot Class -----
class ParkingLot:
    def __init__(self):
        self.spots = []
    
    def add_spot(self, spot):
        self.spots.append(spot)
    
    def show_spots(self):
        for spot in self.spots:
            spot.status()
    
    def park_vehicle(self, vehicle):
        for spot in self.spots:
            if not spot.is_occupied() and spot._fits_vehicle(vehicle):
                return spot.assign_vehicle(vehicle)
        print(f"No suitable spot available for vehicle {vehicle.get_license_plate()}")
        return False
    
    def unpark_vehicle(self, vehicle):
        for spot in self.spots:
            if spot.is_occupied() and spot.get_vehicle() == vehicle:
                spot.remove_vehicle()
                return True
        print(f"Vehicle {vehicle.get_license_plate()} not found in parking lot")
        return False

# ----- Abstract Payment Class and Child Classes -----
class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class CashPayment(Payment):
    def process_payment(self, amount):
        print(f"Paid ₹{amount} via cash")

class CardPayment(Payment):
    def process_payment(self, amount):
        print(f"Paid ₹{amount} via credit/debit card")

class UPIPayment(Payment):
    def process_payment(self, amount):
        print(f"Paid ₹{amount} via UPI")

# ----- Main -----
def main():
    parking_lot = ParkingLot()
    parking_lot.add_spot(ParkingSpot("S1", "S"))
    parking_lot.add_spot(ParkingSpot("M1", "M"))
    parking_lot.add_spot(ParkingSpot("L1", "L"))
    parking_lot.add_spot(ParkingSpot("XL1", "XL"))

    bike = Bike("BIKE123", "Alice", helmet_required=True)
    car = Car("CAR456", "Bob", seats=5)
    suv = SUV("SUV789", "Carol", four_wheel_drive=True)
    truck = Truck("TRK101", "Dave", max_load_capacity=15)
    
    vehicles = [bike, car, suv, truck]
    
    print("\n--- Vehicle Details ---")
    for v in vehicles:
        v.display()
    
    print("\n--- Attempting direct access to sensitive attributes ---")
    try:
        print(bike.__license_plate)
    except AttributeError:
        print("Direct access to private attribute __license_plate fails.")
    print("License plate via getter:", bike.get_license_plate())
    
    print("\n--- Parking Vehicles ---")
    for v in vehicles:
        parking_lot.park_vehicle(v)
    
    print("\n--- Parking Lot Status ---")
    parking_lot.show_spots()
    
    # Unpark and calculate fee
    to_unpark = car
    hours_parked = 4
    print(f"\nUnparking vehicle {to_unpark.get_license_plate()} after {hours_parked} hours.")
    if parking_lot.unpark_vehicle(to_unpark):
        fee = to_unpark.calculate_parking_fee(hours_parked)
        print(f"Parking fee: ₹{fee}")
        
        print("\n--- Processing Payment ---")
        payment_choice = "UPI"  # Simulate user choice
        payment_processor = {
            "Cash": CashPayment(),
            "Card": CardPayment(),
            "UPI": UPIPayment()
        }.get(payment_choice, None)
        
        if payment_processor:
            payment_processor.process_payment(fee)
        else:
            print("Invalid payment method")

if __name__ == "__main__":
    main()
