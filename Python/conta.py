def tamanhopalavra(palavra):
    cont = 0
    for i in palavra:
        cont = cont +1
    print(cont)

palavra = str(input("Digite: "))
print(tamanhopalavra(palavra))

