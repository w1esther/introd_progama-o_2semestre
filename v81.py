# @cikey 834c2e6fa9c10fdc8929a92de4d69a3d
# @sid 20251174010006
# @aid V8.1

# Faça um programa que contém duas funções: uma que escreve uma frase em um arquivo e outra que lê e imprime o conteúdo desse arquivo. A frase deve ser digitada pelo usuário.

caminho = "D:\\Users\\20251174010006\\Downloads\\introd_progama-o_2semestre-main\\bloco8\\v81"

def escreve_frase():
    escrita_usuario = input('escreva algo para o arquivo: ')
    arquivo = open(caminho, 'a')
    arquivo.write(escrita_usuario)
    arquivo.close()

def ler_arquivo():
    arquivo = open(caminho, 'r')
    leitura = arquivo.read()
    arquivo.close()
    return leitura

escrita = escreve_frase()
leitua_do_arquivo = ler_arquivo()

print(escrita)
print(leitua_do_arquivo, end=" ")