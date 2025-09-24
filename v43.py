# @cikey 834c2e6fa9c10fdc8929a92de4d69a3d
# @sid 20251174010006
# @aid V4.3


#begin_inputs
mes = int(input())

#end_inputs
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho','agosto','setembro','outubro','novembro','dezembro']
mes_lista = mes - 1
if 1 > mes or mes > 12:
    print('mes invalido')
else:
    print(lista_meses[mes_lista])