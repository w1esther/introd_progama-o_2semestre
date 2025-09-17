# @cikey 834c2e6fa9c10fdc8929a92de4d69a3d
# @sid 20251174010006
# @aid M2.4


#begin_inputs

valor_compra = float(input('Digite o valor da compra:'))

#end_inputs


valor_a_vista = valor_compra * 0.91
prestação_5_vezes = valor_compra / 5
prestação_10_vezes = (valor_compra * 1.17) / 10

print(valor_a_vista)
print(prestação_5_vezes)
print(prestação_10_vezes)
