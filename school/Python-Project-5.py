class Automobile:
    def __init__(self, make, model, color, year, mileage):
        self.__make = make
        self.__model = model
        self.__color = color
        self.__year = year
        self.__mileage = mileage

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_color(self):
        return self.__color

    def get_year(self):
        return self.__year

    def get_mileage(self):
        return self.__mileage


class Inventory:
    def __init__(self):
        self.__vehicles = []

    def add_vehicle(self, vehicle):
        self.__vehicles.append(vehicle)

    def remove_vehicle(self, make, model, year):
        print("-" * 30) 
        for vehicle in self.__vehicles:
            if vehicle.get_make() == make and vehicle.get_model() == model and vehicle.get_year() == year:
                self.__vehicles.remove(vehicle)
                print("Vehicle removed from inventory:")
                print("Make:", make)
                print("Model:", model)
                print("Year:", year)
                print("-" * 30)  
                return
        print("Vehicle not found in inventory.")

    def display_inventory(self):
        print("-" * 30)
        print("Current Inventory:")
        print("-" * 30)
        for vehicle in self.__vehicles:
            print("Make:", vehicle.get_make())
            print("Model:", vehicle.get_model())
            print("Color:", vehicle.get_color())
            print("Year:", vehicle.get_year())
            print("Mileage:", vehicle.get_mileage())
            print()
            print("-" * 30)


if __name__ == "__main__":
    inventory = Inventory()

    vehicle1 = Automobile("Toyota", "Camry", "Red", 2019, 15000)
    vehicle2 = Automobile("Honda", "Civic", "Blue", 2020, 12000)
    vehicle3 = Automobile("Ford", "Fusion", "Black", 2018, 20000)

    inventory.add_vehicle(vehicle1)
    inventory.add_vehicle(vehicle2)
    inventory.add_vehicle(vehicle3)

    inventory.display_inventory()

    inventory.remove_vehicle("Toyota", "Camry", 2019)

    inventory.display_inventory()