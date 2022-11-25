from turtle import Turtle
import os
t= Turtle()
t.speed(1)

while True:
    print('=============JOGO DA TARTARUGA=============')
    comando = int(input('''Selecione um comando para a tartaruga andar: 
    1- Para frente
    2- Virar à direita
    3- Virar à esquerda
    4- Sair
    R: '''))

    if comando == 1:
        t.forward(int(input('Quanto devo andar? ')))
        os.system('cls')
    elif comando == 2:
        t.right(90)
        t.forward(int(input('Quanto devo andar? ')))
        os.system('cls')
    elif comando ==3:
        t.left(90)
        t.forward(int(input('Quanto devo andar? ')))
        os.system('cls')
    elif comando ==4:
        print('Saindo do Programa!')
        break
    else:
        os.system('cls')
        print('Erro de menu, por favor somente 1,2,3 ou 4 para sair!!')
