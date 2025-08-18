"""
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
- À vista dinheiro/cheque/pix: 10% de desconto
- À vista no cartão: 5% de desconto
- Em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros
"""
valor = float(input("Valor do produto: R$"))

print("""
Forma de Pagamento:
1 - À vista no dinheiro, cheque ou pix
2 - À vista no cartão
3 - Em até 2x no cartão
4 - 3x ou mais no cartão
""")

forma = int(input("Forma de pagamento escolhida: "))

if forma == 1:
    valor_final = valor * 0.9
elif forma == 2:
    valor_final = valor * 0.95
elif forma == 3:
    valor_final = valor
    parcela = valor_final / 2
    print("Você pagará em 2x de R${:.2f}".format(parcela))
elif forma == 4:
    valor_final = valor * 1.20
    vezes = int(input("Em quantas vezes você irá parcelar? "))
    parcela = valor_final / vezes
    print("Sua compra será parcelada em {}x de R${:.2f}".format(vezes, parcela))
else:
    print("Forma de pagamento inválida")
    exit()

print("Valor final: R${:.2f}".format(valor_final))