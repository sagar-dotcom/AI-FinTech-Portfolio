from car_engine import Car, Inventory, Admin, Customer
print("Classes imported successfully!")
my_inventory = Inventory()
carObj1 = Car("Tata", "Nexon", 2025, 1200000, 15000, "Petrol")
carObj2 = Car("Mahindra", "XUV700", 2024, 2500000, 12000, "Diesel")
carObj3 = Car("Hyundai", "Creta", 2025, 1800000, 14000, "Petrol")
carObj4 = Car("Kia", "Seltos", 2024, 1700000, 13000, "Diesel")
carObj5 = Car("Toyota", "Innova", 2023, 3000000, 20000, "Diesel")
carObj6 = Car("Honda", "City", 2025, 1500000, 10000, "Petrol")
carObj7 = Car("Maruti", "Brezza", 2024, 1100000, 16000, "Petrol")
carObj8 = Car("Skoda", "Slavia", 2024, 1600000, 11000, "Petrol")
carObj9 = Car("Volkswagen", "Virtus", 2025, 1650000, 9000, "Petrol")
carObj10 = Car("Tata", "Punch", 2024, 800000, 18000, "Petrol")

my_inventory.add_car(carObj1)
my_inventory.add_car(carObj2)
my_inventory.add_car(carObj3)
my_inventory.add_car(carObj4)
my_inventory.add_car(carObj5)
my_inventory.add_car(carObj6)
my_inventory.add_car(carObj7)
my_inventory.add_car(carObj8)
my_inventory.add_car(carObj9)
my_inventory.add_car(carObj10)

print(f"Total Inventory Value: ₹{my_inventory.get_total_value()}")

for car in my_inventory.cars:
    print(car)

# Admin test
admin1 = Admin("Sagar", "A001", "Super")
# Ab admin se gaadi add karwao
admin1.add_car_to_inventory(my_inventory, carObj1)