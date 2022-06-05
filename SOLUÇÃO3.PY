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
dados2={

}
dado = 0
opção = 0
while opção !=2:
    print('''   [1] ALTERAR DADOS
    [2] SAIR''')
    
    if opção ==1:
         while dado !=6:
            print('''   [1] Código
                [2] Data
                [3] Email
                [4] Nome
                [5] Salario
                [6] Sair''')
            if dado ==1:
                   codigo=str(input('Digite o novo codigo:  '))
                   dados['Data']=codigo
            if dado ==2:
                    data =input('Digite a nova data:')
                    dados['Data']=data
            if dado ==3:
                    email= input("Digite o novo email: ")
                    dados['Email']=email
            if dado ==4:
                    nome = input('Digite o novo nome: ')
                    dados['Nome']=nome
            elif dado ==5:
                   salario= input("Digite o novo salario")
                   dados['Salario']=salario
            elif dado ==6:
                 print('Saindo...')
    elif opção ==2:
        print('Programa encerrado!')    
    opção = int(input("Digite a sua opção: ")) 
    dado = int(input('Qual será o item alterado?'))
