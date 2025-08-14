"""
Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu
"""

import random
from time import sleep

numero = random.randint(0, 5)

adivinha = int(input("Digite um número de 0 a 5 e tente escolher o mesmo que o computador: "))

print("Processando...")
sleep(2)

if numero == adivinha:
    print("Acertou!!")
else:
    print("Errouuuu!! Número escolhido pelo computador: {}".format(numero))