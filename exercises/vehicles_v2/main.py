# 6- Em um arquivo chamado main.py, importe a classe Carro.
from car_v2 import Car
from vehicle_v2 import Vehicle

# 7- No arquivo main.py, instancie três objetos da classe Carro com diferentes características, como marca, modelo e cor.
corsa = Car("Chevrolet", "Corsa", "red")
palio = Car("Fiat", "Palio", "black")
uno = Car("Fiat", "Uno", "gray")

vehicles = [corsa, palio, uno]
print("Vehicles: \n")
for vehicle in vehicles:
    if isinstance(vehicle, Car):
        print(f"{(type(vehicle).__name__).upper()} - {vehicle}")

    else:
        raise Exception("The object is not a valid vehicle.")
