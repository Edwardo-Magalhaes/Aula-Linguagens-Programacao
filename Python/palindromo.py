import string

texto = input("Digite um texto: ")

texto = texto.lower()
texto = texto.replace(" ", "")
texto = texto.translate(str.maketrans('', '', string.punctuation))

texto_invertido = texto[::-1]

if texto == texto_invertido:
    print("É um palíndromo!")
else:
    print("Não é um palíndromo.")