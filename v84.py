# @cikey 834c2e6fa9c10fdc8929a92de4d69a3d
# @sid 20251174010006
# @aid V8.4

cpf_e_nomes = {'nome':[],'cpf':[]}
for n in range(1, 6):
    nome_pessoa = input(f'digite o nome da {n}ª pessoa: ')
    cpf_pessoa = int(input(f'digite o CPF da {n}ª pessoa, sem separação por pontos: '))
    cpf_e_nomes['nome'].append(nome_pessoa)
    cpf_e_nomes['cpf'].append(cpf_pessoa)

with open('C:\\Users\\w1mar\\OneDrive\\Documentos\\GitHub\\introd_progama-o_2semestre\\v84', mode='w') as arquivo:
    for cpf, nome in zip(cpf_e_nomes['cpf'], cpf_e_nomes['nome']):
        arquivo.write(f'{cpf};{nome}\n')

with open('C:\\Users\\w1mar\\OneDrive\\Documentos\\GitHub\\introd_progama-o_2semestre\\v84', mode='r') as arquivo:
    leitura = arquivo.read()
    print(leitura)
# zip "empacota" duas ou mais listas juntando os elementos de mesma posição (mesmo índice)