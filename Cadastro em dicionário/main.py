#FAÇA UM PROGRAMA EM QUE O USUÁRIO PODE CADASTRAR N PESSOAS
#ARMAZENANDO SEU NOME, IDADE E SEXO.

import os #limpa o terminal quando o comando os.system('cls') é executado
pessoas = []
parar = False
while True:
    parar = input('Pressione Enter para cadastrar ou 2 para parar: ')
    if parar == '2':
        break
    else:
        pessoas.append({'Nome':input(f'Digite o nome: ').capitalize(), 'Idade':input(f'Digite a idade: '),'Sexo':input(f'Digite o sexo: ').capitalize()})
        os.system('clear')
print('Quantidade de Pessoas cadastradas: ',len(pessoas)) 
print('Pessoas Cadastradas: ') 
for i in pessoas: 
    print(i)
