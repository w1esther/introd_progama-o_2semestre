# @cikey 834c2e6fa9c10fdc8929a92de4d69a3d
# @sid 20251174010006
# @aid V8.5


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
else:
    None

nome_procurar = input('nome que deseja buscar o telefone: ')

print('deseja salvar os contatos e lê-los em um arquivo externo! em caso da resposta afirmativa de enter e precione precione a tecla "8", se não de enter e precione qualquer outra tecla')
escolha = int(input('opção escolhida: '))

if escolha == 8:
    with open('C:\\Users\\w1mar\\OneDrive\\Documentos\\GitHub\\introd_progama-o_2semestre\\v85', mode='w') as arquivo:
         for contato in lista_contatos:
            arquivo.write(f"{contato['nome']};{contato['telefone']}\n")


print(novo_contato())
print(consulta_por_nome(nome_procurar))