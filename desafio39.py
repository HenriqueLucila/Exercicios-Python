"""
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
- Se ele ainda vai se alistar ao serviço militar.
- Se é a hora de se alistar.
- Se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
"""
from datetime import datetime

nascimento = int(input("Em qual ano você nasceu? "))

ano_atual = datetime.today().year
idade = ano_atual - nascimento

if(idade < 18):
    saldo = 18 - idade
    print("Ainda não é hora de se alistar. Faltam {} anos para seu alistamento.".format(saldo))
elif(idade == 18):
    print("Hora de se alistar ao serviço militar.")
else:
    saldo = idade - 18
    ano_alistamento = ano_atual - saldo
    print("Você já passou do tempo do alistamento. Já fazem {} anos do ano de seu alistamento.\nSeu alistamento foi em {}.".format(saldo, ano_alistamento))