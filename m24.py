# @cikey 834c2e6fa9c10fdc8929a92de4d69a3d
# @sid 20251174010006
# @aid V2.4


#begin_inputs

valor_compra = float(input('Digite o valor da compra:'))

#end_inputs


valor_a_vista = valor_compra * 0.91
prestação_5_vezes = valor_compra / 5
prestação_10_vezes = (valor_compra * 1.17) / 10

print(round(valor_a_vista, 2))
print(round(prestação_5_vezes, 2))
print(round(prestação_10_vezes, 2))