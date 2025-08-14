# O mesmo professor do desadio anterior quer sortear a ordem de apresentação de trabalho dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random

alunos = ['Henrique','Duda','Rodrigo','Sandra']

print("Alunos presentes: {}".format(alunos))

random.shuffle(alunos)

print("Ordem de apresentação dos trabalhos: {}\n".format(alunos))