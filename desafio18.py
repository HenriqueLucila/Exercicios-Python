# Faça um programa que leia um ângulo qualquer e mostre na tela o valer do seno, cosseno e tangente desse ângulo.

from math import cos, sin, tan, radians

num = float(input("Digite um ângulo em graus: "))

rad = radians(num)

print("Seno: {:.2f} \n Cosseno: {:.2f} \n Tangente: {:.2f}".format(sin(rad), cos(rad), tan(rad)))