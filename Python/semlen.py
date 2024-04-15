def conta_palavras(lista):
    contador = 0
    for palavra in lista:
        contador = contador + 1
    print(f'quantidade de palavras na lista: {contador}')

def conta_letras(lista):
    contador_palavra = 1
    for palavra in lista:
        contador_letras = 0
        for letra in palavra:
            contador_letras = contador_letras + 1
        print(f'quantidade de letras na palavra {contador_palavra}: {contador_letras}')
        contador_palavra = contador_palavra + 1

# Testa as funções com a lista fornecida
lista = ["oi", "tubem", "palavra", "quadro","FAMENGOOOO","VASCOOO"]
conta_palavras(lista)
conta_letras(lista)
