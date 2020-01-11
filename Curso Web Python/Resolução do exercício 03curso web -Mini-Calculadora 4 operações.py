# Mini Calculadora 3.0

print('-----------  Mini Calculadora ------------- \n')

num1 = float(input('Informe o primeiro número: '))
num2 = float(input('Informe o segundo número: '))

print('----------------------------------------------')
operacao = input('Informe a operação que deseja realizar ("+" para somar, "-" para subtrair):')
print('----------------------------------------------')
if operacao == '+':
    print ('Resultado: ', num1 + num2)
elif operacao == '-':
    print ('Resultado:', num1 - num2 )
elif operacao == '*':
    print('Resultado: ', num1 * num2)
elif operacao == '/':
    print('Resultado: ', num1 / num2)
else:
    print('Operação Inválida !!!')
print('\n-----------  Mini Calculadora -------------')
