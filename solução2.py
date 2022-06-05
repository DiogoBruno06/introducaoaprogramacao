nome = str(input('Digite o nome do Funcionario: '))
data = str(input('Digite a sua data de admissão: '))
codigo = str(input("Digite o seu codigo "))
salario = str(input('Digite o seu salario: '))
email = str(input('Digite o seu e-mail: '))
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
nnome = input('Digite o novo funcionario: ')
ndata = input("Digite a data de admissão: ")
ncodigo = input("Digite o codigo: ")
nsalario = input('Digite o salario: ')
nemail= input('Digite o email: ')
dados['Codigo'] =nome,ncodigo
dados['Data']= data,ndata
dados['Email']= email,nemail
dados['Nome']= nome,nnome
dados['Salario']= salario,nsalario
for x, i in dados.items():
    print ('{}:{}'.format(x,i))
print('DADOS CADASTRADOS...')
z = dados.get('Nome')
print('Os nomes cadastrados são {}'.format(z))
print('-'*100)
dado = 0
opção = 0
opção = int(input('Digite o opção: '))
if opção <=2: 
    print('''[1] ALTERAR DADOS
    [2]REMOVER FUNCIONARIO''')
    
    if opção ==1:
         while dado !=5:
            print('''   [1] Código
                [2] Data
                [3] Email
                [4] Nome
                [5] Salario
                [6] Sair''')
            dado = int(input('Qual será o item alterado: '))
            if dado ==1:
                    codigo=str(input('Digite o novo codigo:  '))
                    dados['Codigo']=codigo
            elif dado ==2:
                    data =input('Digite a nova data:')
                    dados['Data']=data
            elif dado ==3:
                    email= input("Digite o novo email: ")
                    dados['Email']=email
            elif dado ==4:
                    nome = input('Digite o novo nome: ')
                    dados['Nome']=nome
            elif dado ==5:
                    salario= input("Digite o novo salario")
                    dados['Salario']=salario
    if opção ==2:
        dados['Codigo']=None
        dados['Data']=None
        dados['Email']=None
        dados['Nome']=None
        dados['Salario']=None
        print(dados)

