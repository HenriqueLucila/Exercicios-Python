"""
Refaça o desafio 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- Equilátero: todos os lados iguais
- Isósceles: dois lados iguais
- Escaleno: todos os lados diferentes
"""

lado1 = int(input("Tamanho do lado 1: "))
lado2 = int(input("Tamanho do lado 2: "))
lado3 = int(input("Tamanho do lado 3: "))

if (lado1 + lado2) > lado3 and (lado1 + lado3) > lado2 and (lado2 + lado3) > lado1:
    print("É possível formar um triângulo")

    if lado1 == lado2 == lado3:
        print("O triângulo formado será EQUILÁTERO")
    elif lado1 != lado2 != lado3 != lado1:
        print("O triângulo formado será ESCALENO")
    else:
        print("O triângulo formado será ISÓSCELES")

else:
    print("Não é possível formar um triângulo")