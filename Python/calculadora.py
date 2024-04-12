def soma (a, b):
    return (a + b)
def sub (a, b):
    return (a - b)
def mult (a, b):
    return (a*b)
def div (a, b):
    return (a/b)
valor1 = 0
valor2 = 0
operador = 0
while valor1 != -1 and valor2 != -1  and operador != -1:
    valor1 = int(input("digite um valor: "))      
    operador = str(input("digite um operador: "))
    valor2 = int(input("digite outro valo5r: "))
    resultado = 0
    if operador == '+':
        resultado = soma (valor1, valor2)
    elif operador == '-':
        resultado = sub (valor1, valor2)
    elif operador == '*':
        resultado = mult (valor1, valor2)
    elif operador == '/':
        resultado = div (valor1, valor2)
    else:
        print('operador inválido')
    print(resultado)