# @cikey 834c2e6fa9c10fdc8929a92de4d69a3d
# @sid 20251174010006
# @aid V6.3


#begin_inputs
n = int(input())
#end_inputs

def inverso(n):
    n_string = str(n)
    invertido = n_string[::-1]
    return invertido


numero_invertido = inverso(n)
print(numero_invertido)