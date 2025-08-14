"""
Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite.
"""

velocidade = int(input("Velocidade do carro em Km/h: "))

if velocidade <= 80:
    print("Você passou dentro do limite de velocidade.")
else:
    multa = (velocidade - 80) * 7
    print("Você passou acima do limite de velocidade da via. \n Multa: R${},00".format(multa))