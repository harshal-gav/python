class Car:
    def __init__(self, model, isautomatic):
        self.model = model
        self.isautomatic = isautomatic

    def get_model(self):
        return self.model

    def get_isautomatic(self):
        return self.isautomatic

    def __repr__(self):
        return f"Car(model='{self.model}', isautomatic={self.isautomatic})"



car1 = Car("Tesla Model S", True)
car2 = Car("Ford Mustang", False)
car3 = Car("Honda Civic", True)
car4 = Car("BMW 3 Series", False)
car5 = Car("Toyota Corolla", True)


car_list = [car1, car2, car3, car4, car5]


automatic_car_list = [car for car in car_list if car.get_isautomatic()]


print("All Cars:")
print(car_list)

print("Automatic Cars:")
print(automatic_car_list)
