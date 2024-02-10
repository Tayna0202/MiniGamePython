import os

jogador = {"nome": "Python", "x": 0, "y": 0}

def andar(direcao):
    if direcao == "d":
        jogador['x'] += 1
    elif direcao == "a":
        jogador['x'] -= 1
    elif direcao == "w":
        jogador['y'] -= 1
    elif direcao == "s":
        jogador['y'] += 1

while True:
    os.system('cls')

    print("------------------------")
    for y in range(5):
        print("\n")
        for x in range(10):
            if jogador['x'] == x and jogador['y'] == y:
                print("🐲", end="")
            else:
                print("🟩", end="")
    print("------------------------")

    direcao = input("Mova seu personagem (W, S, D, A): ")
    andar(direcao)
