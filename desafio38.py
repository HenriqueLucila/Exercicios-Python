"""
Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
- O primeiro valor é o maior
- O segundo valor é o maior
- Não existe valor maior, os dois são iguais
"""

n1 = int(input("Digite o 1° número: "))
n2 = int(input("Digite o 2° número: "))

if(n1 > n2):
    print("O primeiro valor é o maior")
elif(n2 > n1):
    print("O segundo valor é o maior")
else:
    print("Não existe valor maior, os dois são iguais")