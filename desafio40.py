"""
Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
- Média abaixo de 5.0: Reprovado
- Média entre 5.0 e 6.9: Recuperação
- Média 7.0 ou superior: Aprovado
"""
n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))

media = (n1 + n2) / 2

if media < 5.0:
    print("Média: {:.2f} \nSituação final: REPROVADO.".format(media))
elif 7 > media > 5.0:
    print("Média: {:.2f} \nSituação final: RECUPERAÇÃO.".format(media))
elif media >= 7.0:
    print("Média: {:.2f} \nSituação final: APROVADO.".format(media))