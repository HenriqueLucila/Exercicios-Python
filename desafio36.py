"""
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
"""

valor_casa = float(input("Qual o valor da casa? R$"))
salario = float(input("Qual o salário do comprador? R$"))
duracao_emprestimo = int(input("Em quantos anos o empréstimo será pago? "))

prestacao_mensal = valor_casa / (duracao_emprestimo * 12)

limite = salario * 0.3

if (prestacao_mensal <= limite):
    print("Empréstimo aceito!! \nPrestação mensal: {:.2f}".format(prestacao_mensal))
else:
    print("Empréstimo negado. \nPois a prestação mensal ficaria em R${:.2f}, que é acima do seu limite: R${:.2f} (30% do salário)".format(prestacao_mensal, limite))