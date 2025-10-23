# @cikey 834c2e6fa9c10fdc8929a92de4d69a3d
# @sid 20251174010006
# @aid V7.2


#begin_inputs

letras = input().split()
palavra = input()

#end_inputs

def adivinhou_palavra(letras, palavra):
    for n in palavra:
        if n not in letras:
            return False
    return True

resultado = adivinhou_palavra(letras, palavra)

print(resultado)