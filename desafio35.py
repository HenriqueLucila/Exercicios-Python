# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

lado1 = int(input("Tamanho do lado 1: "))
lado2 = int(input("Tamanho do lado 2: "))
lado3 = int(input("Tamanho do lado 3: "))

if (lado1 + lado2) > lado3 and (lado1 + lado3) > lado2 and (lado2 + lado3) > lado1:
    print("É possível formar um triângulo")
else:
    print("Não é possível formar um triângulo")