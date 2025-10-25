# @cikey 834c2e6fa9c10fdc8929a92de4d69a3d
# @sid 20251174010006
# @aid V7.4


lista_contatos = []

nome = input('digite seu nome: ')
telefone = int(input('digite seu número de telefone: '))

def novo_contato():
    contato = {'nome': nome, 'telefone': telefone}
    lista_contatos.append(contato)
    return 'contato adicionado!'

def consulta_por_nome(nome_pessoa):
    for contato in lista_contatos:
        if contato['nome'] == nome_pessoa:
            return contato['telefone']
    return "Contato não encontrado!"

print('se deseja adicionar uma novo contato digite "sim" ')

opcao = input('digite: ')

if opcao == 'sim':
    adicionar_novo_contato = opcao 

while adicionar_novo_contato == 'sim':
    nome = input('digite seu nome: ')
    telefone = int(input('digite seu número de telefone: '))
    novo_contato()
    print('se deseja adicionar uma novo contato digite "sim" ')
    opcao = input('digite: ')
    adicionar_novo_contato = opcao 

nome_procurar = input('nome que deseja buscar o telefone: ')

print(novo_contato())
print(consulta_por_nome(nome_procurar))