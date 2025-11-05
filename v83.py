# @cikey 834c2e6fa9c10fdc8929a92de4d69a3d
# @sid 20251174010006
# @aid V8.3

origem = 'D:\\Users\\20251174010006\\Downloads\\introd_progama-o_2semestre-main\\bloco8\\v82'
destino = 'D:\\Users\\20251174010006\\Downloads\\introd_progama-o_2semestre-main\\bloco8\\v83'

with open(origem, 'r') as arquivo1, open(destino, 'w') as arquivo2:
    arquivo2.write(arquivo1.read())

print(destino)