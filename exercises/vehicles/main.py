# 8- Crie um Arquivo Main (main.py): Crie um arquivo chamado main.py no mesmo diretório que suas classes.
# 9- Importe e Instancie Objetos: No arquivo main.py, importe as classes Carro e Moto.

from cars import Car
from motorcycles import Motorcycle
from vehicle import Vehicle


# 10-  Em seguida, crie três instâncias de Carro e Moto com diferentes marcas, modelos, quantidade de portas e tipos(esportiva ou casual).

# Car
fusca = Car("Volkswagen", "Fusca", 2)
clio = Car("Renault", "Clio", 4)
pegeout_2008 = Car("Pegeout", "Pegeout 2008", 4)

# Motorcycle
suzuki = Motorcycle("Suzuki", "Hayabusa", "sports")
honda = Motorcycle("Honda", "CB1000 Hornet", "casual")
kawasaki = Motorcycle("Kawasaki", "Ninja 400", "sports")


# 11- Exiba as Informações: Para cada instância, imprima no console as informações utilizando o método str.

print(fusca)
print(clio)
print(pegeout_2008)
print()
print(suzuki)
print(honda)
print(kawasaki)
print()

# answer 11 - better way:

vehicle_list = [fusca, clio, pegeout_2008, suzuki, honda, kawasaki]
print("VEHICLES:\n")
for vehicle in vehicle_list:
    if isinstance(vehicle, Vehicle):
        print(f"{(type(vehicle).__name__).upper()} - {vehicle}")
    else:
        raise Exception("Object is not a valid vehicle.")
