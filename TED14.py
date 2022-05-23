LISTA = {
    'FUNCIONARIO': 'Diogo',
    'SALARIO' :'$ 9,500',
    'CODIGO' :'14577',
    'E-MAIL' :'diogo123@iesp.com',
    'DATA' :'14/02/2020',
}
for x, i in LISTA.items():
    print('{}:{}'.format(x,i))
    print('-'*50)
LISTA.update({'FUNCIONARIO': 'Messias,Diogo', 'E-MAIL' : 'messias123@iesp.com,diogo123@iesp.com'})
for x, i in LISTA.items():
    print('{}:{}'.format(x,i))
print('-'*100)
print('CADASTRANDO NOVOS DADOS...')
print("-"*100)
print('FUNCIONARIOS CADASTRADOS')
print(LISTA['FUNCIONARIO'])
print('-'*100)
LISTA.update({'FUNCIONARIO': 'Messias', 'E-MAIL':'messias123@iesp.com'})
for x ,i in LISTA.items():
    print('{}:{}'.format(x,i))
print('FUNCIONARIO EXCLUIDO COM SUCESSO...')
print("-"*100)
LISTA.update({'SALARIO':'$ 2,50'})
print('AJUSTANDO SALARIO...')
print('-'*100)
for x, i in LISTA.items():
    print('{}:{}'.format(x,i))
print('-'*100)

print('REGISTRO TERMINADO COM SUCESSO')
print('GRUPO: DIOGO BRUNO MARQUES NEVES')