# @cikey 834c2e6fa9c10fdc8929a92de4d69a3d
# @sid 20251174010006
# @aid V6.4


#begin_inputs

#end_inputs

valor_dado = int(input('valor sorteado no dado: '))

if valor_dado == 7 or valor_dado == 11:
    print('Voce ganhou!')
elif valor_dado == 2 or valor_dado == 3 or valor_dado == 12:
    print('Voce perdeu!')
else:
    ponto = valor_dado
    valor_dado = int(input())
    while valor_dado != ponto:
        valor_dado = int(input())
        if valor_dado == 7:
            valor_dado = int(input())
            if valor_dado == ponto:
                print('Voce perdeu!')
    print('Voce ganhou!')  