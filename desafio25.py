# Crie um programa que leia o nome de uma pessoa e difa se ela tem "Silva no nome"

nome = str(input("Digite seu nome completo: ")).strip()

nome = nome.upper()
nome = nome.split()

print("Tem 'Silva' no nome? {}".format('SILVA' in nome))