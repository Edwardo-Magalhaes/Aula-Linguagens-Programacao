nome = input("Nome: ")
posicao = int(input("Posição: "))
letra = nome[posicao]

if letra == 'r':
    nome = nome[:posicao] + 's' + nome[posicao+1:]
elif letra == 'm':
    nome = nome[:posicao] + 'n' + nome[posicao+1:]
else:
    nome = nome[:posicao] + nome[posicao+1:]

print("Novo:", nome)
