valor1 = int(input())

while valor1 != "-1" or valor2 != "-1":
    operador = input()
    valor2 = int(input())
    if valor2 == "-1":
        break

    if operador == '+':
        resultado = valor1 + valor2
    elif operador == '-':
        resultado = valor1 - valor2
    elif operador == '*':
        resultado = valor1 * valor2
    elif operador == '/':
        resultado = valor1 / valor2
    else:
        print('Operador inválido')
        continue
    print(resultado)
    valor1 = int(input())
