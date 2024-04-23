# Variável global para o tabuleiro
tabuleiro = [[" "]*3 for _ in range(3)]

def exibir_menu():
    print("----------------------------------")
    print("Seja bem-vindo ao jogo da velha!")
    print("----------------------------------")

def imprimir_tabuleiro():
    for i in range(3):
        for j in range(3):
            print(tabuleiro[i][j], end="")
            if j < 2:
                print("|", end="")
        print()
        if i < 2:
            print("-----")

def marca_posicao(jogador, linha, coluna):
    if tabuleiro[linha][coluna] != " ":
        print("Posição inválida! Por favor, escolha outra posição.")
        return False
    tabuleiro[linha][coluna] = jogador
    return True

def verificar_vencedor(jogador):
    # Verificar linhas
    for i in range(3):
        if tabuleiro[i] == [jogador, jogador, jogador]:
            return True
    # Verificar colunas
    for i in range(3):
        if tabuleiro[0][i] == jogador and tabuleiro[1][i] == jogador and tabuleiro[2][i] == jogador:
            return True
    # Verificar diagonais
    if tabuleiro[0][0] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][2] == jogador:
        return True
    if tabuleiro[0][2] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][0] == jogador:
        return True
    return False

def jogar():
    exibir_menu()
    jogador = "X"
    jogadas = 0
    while jogadas < 9:
        imprimir_tabuleiro()
        print(f"É a vez do jogador {jogador}, em qual posição você deseja jogar?")
        linha, coluna = map(int, input("> ").split())
        if marca_posicao(jogador, linha, coluna):
            jogadas += 1
            with open('tabuleiro.txt', 'w') as f:
                for i in range(3):
                    for j in range(3):
                        f.write(tabuleiro[i][j])
                        if j < 2:
                            f.write("|")
                    f.write("\n")
                    if i < 2:
                        f.write("-----\n")
            if verificar_vencedor(jogador):
                print(f"O jogador {jogador} venceu!")
                break
            jogador = "O" if jogador == "X" else "X"  # Troca o jogador
    else:
        print("Empate!")

if __name__ == "__main__":
    jogar()
