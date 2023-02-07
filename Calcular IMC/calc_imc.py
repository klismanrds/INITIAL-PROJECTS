import os

while True:
    print('='*10+'Calculadora IMC'+'='*10)
    nome = input('Digite o seu nome: ')
    peso = float(input('Entre com o seu peso: '))
    altura = float(input('Entre com a sua altura: (Exemplo: 1.75) '))
    imc = peso/altura**2
    print(f'O resultado do imc foi: {imc:,.0f}')

    if imc < 18.5:
        print(f'{nome} Sua classificação é: Magreza!!!')
    elif imc > 18.5 and imc < 24.9:
        print(f'{nome} Sua classificação é: Normal!!!')
    elif imc > 24.9 and imc < 30:
        print(f'{nome} Sua classificação é: Sobrepeso, Procure um nutricionista!!!')
    elif imc > 29.9 and imc <40:
        print(f'{nome} Sua classificação é: Obesidade, Procure um médico!!!')
    else:
        print(f'{nome} Sua classificação é: Obesidade Grave Procure um médico!!!')
    decisao = int(input('Deseja calcular novamente? 1-SIM / 2-NÃO: '))
    if decisao == 1:
        print('Reiniciando...')
        os.system("cls")
        continue
    elif decisao == 2:
        print('Finalizando...')
    if decisao != 1 and decisao != 2:
        os.system('cls')            
    break

