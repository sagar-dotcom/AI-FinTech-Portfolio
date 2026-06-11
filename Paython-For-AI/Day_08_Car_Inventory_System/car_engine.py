class Car:
    def __init__(self, brand, model, year, price, mileage, fuel_type):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price
        self.mileage = mileage
        self.fuel_type = fuel_type
        self.is_sold = False
        self.stock = 1

    def __str__(self):
        return f"{self.year} {self.brand} {self.model} ({self.fuel_type}) - ₹{self.price}"
    
class Inventory:
    def __init__(self):
        self.cars = []
    
    def add_car(self, car_obj):
        self.cars.append(car_obj)
        print(f"Added new car in inventory: {car_obj.brand} {car_obj.model}")

    def sell_car(self, model_name):
        for car in self.cars: # Yahan 'car' singular hona chahiye
            if car.model == model_name and not car.is_sold:
                car.is_sold = True
                print(f"Sold: {car.brand} {car.model}")
                return
        print("Car not found or already sold.") # Loop ke bahar

    def get_total_value(self):
        total = 0
        for car in self.cars:
            if not car.is_sold:
                total += car.price
        return total

class User:
    def __init__(self, name, user_id): # Yahan __init__ do underscore ke saath
        self.name = name
        self.user_id = user_id

class Admin(User):
    def __init__(self, name, user_id, admin_level):
        super().__init__(name, user_id)
        self.admin_level = admin_level

    def add_car_to_inventory(self, inventory, car):
        inventory.add_car(car)
        print(f"Admin {self.name} (Level: {self.admin_level}) ne gaadi add ki.")

class Customer(User):
    def __init__(self, name, user_id, email):
        super().__init__(name, user_id)
        self.email = email

    def buy_car(self, inventory, model_name):
        inventory.sell_car(model_name)
        print(f"Customer {self.name} ne car khareedi.")