# @cikey 834c2e6fa9c10fdc8929a92de4d69a3d
# @sid 20251174010006
# @aid V7.3

from random import randint

lista = []

for n in range(25):
    while True:
        num_sorteado = randint(1, 40)
        if num_sorteado not in lista:
            lista.append(num_sorteado)
            break

lista_ordenada = sorted(lista)

print(lista_ordenada)