# @cikey 834c2e6fa9c10fdc8929a92de4d69a3d
# @sid 20251174010006
# @aid V6.1


#begin_inputs

#end_inputs

	
import random

lista = []

for n in range(6):
    numero_sorteado = random.randint(1, 50)
    lista.append(numero_sorteado)
print(lista)