# @cikey 834c2e6fa9c10fdc8929a92de4d69a3d
# @sid 20251174010006
# @aid V7.1


#begin_inputs

letras = input().split(' ')

#end_inputs

from string import ascii_lowercase

def letras_disponiveis(letras):
    letras_para_chutar = []
    for n in ascii_lowercase:
        if n not in letras:
            letras_para_chutar.append(n)
    print(letras_para_chutar)


disponiveis = letras_disponiveis(letras)





