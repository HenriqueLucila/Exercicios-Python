"""
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
- Abaixo de 18.5: Abaixo do peso
- Entre 18.5 e 25: Peso ideal
- Entre 25 e 30: Sobrepeso
- Entre 30 e 40: Obesidade
- Acima de 40: Obesidade mórbida
"""
peso = float(input("Peso (em KG): "))
altura = float(input("Altura (em metros): "))

imc = peso / (altura * altura)

print("IMC: {:.2f} \nStatus segundo o IMC:".format(imc))

if imc < 18.5:
    print("Abaixo do peso")
elif imc >= 18.5 and imc < 25:
    print("Peso ideal")
elif imc >= 25 and imc < 30:
    print("Sobrepeso")
elif imc >= 30 and imc < 40:
    print("Obesidade")
elif imc >= 40:
    print("Obesidade Mórbida")