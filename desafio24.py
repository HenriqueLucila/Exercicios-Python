# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo"

cidade = str(input("Nome da sua cidade: ")).strip()

cidade = cidade.upper()
cidade = cidade.split()

print("Cidade começa com o nome Santo? {}".format('SANTO' in cidade[:5]))