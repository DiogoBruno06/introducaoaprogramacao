nome = input('Digite o nome do Funcionario: ')
data = input('Digite a sua data de admissão: ')
codigo = input("Digite o seu codigo ")
salario = input('Digite o seu salario: ')
email = input('Digite o seu e-mail: ')
dados= {
    'Nome': nome,
    'Data': data,
    'Codigo': codigo,
    'Salario': salario,
    'Email': email
}
print('CADASTRANDO DADOS...')
print('-'*100)
for x,i in dados.items():
    print('{}:{}'.format(x,i))
print('-'*100)    
novo = input('Digite o novo funcionario: ')
dados= {
    'Nome': nome,
    'Data': data,
    'Codigo': codigo,
    'Salario': salario,
    'Email': email
}
dados['Nome'] = nome,novo
for x,i in dados.items():
    print('{}:{}'.format(x,i))
print('NOVO FUNCIONARIO CADASTRADO!!!!')
print("-"*100)
print('FUNCIONARIOS CADASTRADOS')
print(dados['Nome'])
del dados ['Nome']
print(dados)