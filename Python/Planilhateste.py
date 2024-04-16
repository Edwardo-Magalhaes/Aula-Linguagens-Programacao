import csv
from datetime import datetime

nome_buscar = input("Digite um nome: ")

with open('alunos.csv', 'r') as arquivo:
    leitor = csv.reader(arquivo)
    next(leitor) 
    for linha in leitor:
        nome, data_nascimento, matricula = linha.strip("\n").split(",")
        if nome == nome_buscar:
            data_nascimento = datetime.strptime(data_nascimento, '%d/%m/%Y')
            idade = datetime.now().year - data_nascimento.year
            print(f'Nome: {nome}, Idade: {idade}')
