# Crie um programa que faça o computador jogar Jokenpô com você
import random

print("""
Brincadeira do Jokenpô:
1 - PEDRA
2 - PAPEL
3 - TESOURA
""")

jogador = int(input("Escolha sua jogada: "))

maquina = random.randint(1, 3)

if jogador == 1 and maquina == 1:
    print("Empate! Os dois escolheram pedra")
elif jogador == 1 and maquina == 2:
    print("Você perdeu! A máquina escolheu papel")
elif jogador == 1 and maquina == 3:
    print("Parabéns, você ganhou! A máquina escolheu tesoura")
elif jogador == 2 and maquina == 1:
    print("Parabéns, você ganhou! A máquina escolheu pedra")
elif jogador == 2 and maquina == 2:
    print("Empate! Os dois escolheram papel")
elif jogador == 2 and maquina == 3:
    print("Você perdeu! A máquina escolheu tesoura")
elif jogador == 3 and maquina == 1:
    print("Você perdeu! A máquina escolheu pedra")
elif jogador == 3 and maquina == 2:
    print("Parabéns, você ganhou! A máquina escolheu papel")
elif jogador == 3 and maquina == 3:
    print("Empate! Os dois escolheram tesoura")
else:
    print("Escolha uma jogada válida!")