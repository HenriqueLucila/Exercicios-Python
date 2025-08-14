"""
Faça um programa que leia uma frase pelo teclado e mostre:
- Quantas vezes aparece a letra 'A'
- Em que posição ela aparece a primeira vez.
- Em que posição ela aparece a última vez.
"""

frase = str(input("Digite uma frase: ")).strip()

frase = frase.upper()

print("Quantidade de letras 'A' na frase: {}".format(frase.count("A")))
print("Primeira posição que a letra 'A' aparece: {}".format(frase.find("A")))
print("Última posição que a letra 'A' aparece: {}".format(frase.rfind("A")))