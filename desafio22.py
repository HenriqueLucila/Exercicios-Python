"""
Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas
- O nome com todas as letras minúsculas
- Quantas letras ao todo (sem considerar espaços)
- Quantas letras possui o primeiro nome
"""

nome = str(input("Digite seu nome: "))

nome_sem_espaco = nome.replace(" ", "")
primeiro_nome = nome.split()

print("Nome com letras maiúsculas: {}".format(nome.upper()))
print("Nome com letras minúsculas: {}".format(nome.lower()))
print("Quantas letras este nome possui: {}".format(nome_sem_espaco.__len__()))
print("Quantas letras tem o primeiro nome: {}".format(primeiro_nome[0].__len__()))