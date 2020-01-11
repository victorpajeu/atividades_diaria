# Exercício IMC

print('------------  Calculador de IMC  ------------ \n')

peso = float(input('Informe o seu peso: '))
altura = float(input('Informe a sua altura: '))

imc = peso / altura**2

if imc < 18.5:
    print('\n Abaixo do peso !!!')
elif ((imc >= 18.5)and(imc < 25)):
    print('\n Peso normal !!!')
elif ((imc >= 25)and( imc < 30)):
    print('\n Acima do peso !!!')
elif imc >= 30:
    print('\n Obeso !!!')


print('\n------------  Calculador de IMC  ------------ ')
