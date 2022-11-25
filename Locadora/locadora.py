import os
from datetime import datetime

carros = []
carro = []

dia = datetime.now().day
mes = datetime.now().month
ano = datetime.now().year


class Carro:
    def __init__(self, marca, modelo, cor):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor


while True:
    menu_escolha = int(
        input('''    ========MENU PRINCIPAL========
    Deseja Cadastrar um veículo? 
    1 = CADASTRAR CARRO
    2 = CONSULTAR CARROS CADASTRADOS
    3 = SALVAR EM UM ARQUIVO
    4 = SAIR DO PROGRAMA
    R = '''))

    if menu_escolha == 1:
        os.system("clear")
        print('=' * 20, 'CADASTRO DE CARROS', '=' * 20)
        carro1 = Carro(input('DIGITE A MARCA: '), input('DIGITE O MODELO: '),
                       input('DIGITE A COR: '))
        carro.append(carro1.marca)
        carro.append(carro1.modelo)
        carro.append(carro1.cor)
        os.system("clear")
        print(f'CARRO CADASTRADO COM SUCESSO!!!\n {carro}')
        carros.append(carro)
        carro = []

    elif menu_escolha == 2:
        os.system("clear")
        print(f'CARROS CADASTRADOS: {len(carros)}')
        for x in carros:
            print(x)
        input('Digite qualquer tecla para voltar ao menu: ')
        os.system("clear")

    elif menu_escolha == 3:
        with open('carros.txt', 'a') as arquivo:
            arquivo.write(f'\n{dia}/{mes}/{ano}')
            for x in carros:
                arquivo.write(f'\n{x}')
            carros = []
            carro = []
            print('ARQUIVO SALVO COM SUCESSO!!')
            input('Digite qualquer tecla para voltar ao menu: ')
            os.system("clear")

    elif menu_escolha == 4:
        os.system("clear")
        print('Saindo do programa! \n Obrigado por testar =)')
        break

    elif menu_escolha != 1 and menu_escolha != 2 and menu_escolha != 3:
        os.system("clear")
        print('POR FAVOR, SOMENTE NÚMEROS DE 1 A 3!! ')
