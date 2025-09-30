# @cikey 834c2e6fa9c10fdc8929a92de4d69a3d
# @sid 20251174010006
# @aid V5.2


#begin_inputs


#end_inputs

minutos = 0

distancia_tartaruga = 1*minutos + 500
distancia_lebre = 10*minutos

while distancia_tartaruga > distancia_lebre:
    minutos += 1
    distancia_tartaruga = 1*minutos +500
    distancia_lebre = 10*minutos
print(minutos)