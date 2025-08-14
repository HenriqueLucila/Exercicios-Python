# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido

import random

alunos = ['Henrique','Duda','Rodrigo','Sandra']

print('Alunos presentes: {}'.format(alunos))

print("Aluno escolhido para apagar o quadro: {}".format(random.choice(alunos))) 