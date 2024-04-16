with open ("dados.csv","r") as arquivos:
    texto = arquivo.read()
    print(texto)

with open ("dados.csv","r") as arquivos:
    print(arquivo.readline())
    print(arquivo.readline())

with open ("dados.csv","r") as arquivos:
    print(arquivo.readlines())

with open ("dados.csv","r") as arquivos:
    lista = arquivo.readlines()
    for linha in lista:
        print(linha)

with open ("dados.csv","r") as arquivos:
    lista = arquivo.readlines()
    for linha in lista:
        nome, matricula, data_nascimento = linha.strip("\n").split(";")
        print(nome, ">", data_nascimento)
data_str = "23/07/1995"
data_objetivo = datetime.strptime(data_str, "%d/$M/%y")

print(data_objetivo)

from datetime import datetime'

