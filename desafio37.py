"""
Escreva um programa que leia um número inteiro e peça para o usuário escolher qual será a base de conversão:
- 1 para binário
- 2 para octal
- 3 para hexadecimal
"""

numero = int(input("Digite um número inteiro: "))
base = int(input("1 para binário \n2 para octal \n3 para hexadecimal \nQual será a base para conversão do número? "))

if (base == 1):
    print("Número digitado convertido para binário: {}".format(bin(numero)[2:]))
elif (base == 2):
    print("Número digitado convertido para octal: {}".format(oct(numero)[2:]))
elif (base == 3):
    print("Número digitado convertido para hexadecimal: {}".format(hex(numero)[2:]))
else:
    print("Digite um número válido para seguir com a conversão!")