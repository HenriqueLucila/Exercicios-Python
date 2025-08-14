"""
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

Ex: Digite um número: 1834
- Unidade: 4
- Dezena: 3
- Centena: 8
- Milhar: 1
"""

num = str(input("Digite um número de 0 a 9999: ")).zfill(4)

print("Unidade: {}".format(num[3]))
print("Dezena: {}".format(num[2]))
print("Centena: {}".format(num[1]))
print("Milhar: {}".format(num[0]))

"""
Ou desta maneira:
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
"""