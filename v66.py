# @cikey 834c2e6fa9c10fdc8929a92de4d69a3d
# @sid 20251174010006
# @aid V6.6

from random import randint
n = int(input('tente adivinhar um numero de 1 a 1.000.000: '))

numero_secreto = randint(1, 1000000)

tentativas = 0

while n != numero_secreto:
    if n < numero_secreto:
        print('o valor secreto e maior! Tente novamente')
        n = int(input('tente adivinhar um numero de 1 a 100: '))
    elif n > numero_secreto:
        print('o valor secreto e menor! Tente novamente')
        n = int(input('tente adivinhar um numero de 1 a 100: '))
    tentativas += 1
    if tentativas == 21:
        break

if n == numero_secreto:
    print(f'Parabens, voce acertou! O numero secreto e: {numero_secreto} e voce acertou em {tentativas} tentativas!')
else: 
    print('voce perdeu!')
