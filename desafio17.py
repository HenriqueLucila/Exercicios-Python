# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento.

import math

cat_oposto = float(input("Comprimento do Cateto Oposto em cm: "))
cat_adjacente = float((input("Comprimento do Cateto Adjacente em cm: ")))

hipotenusa = math.sqrt(((pow(cat_oposto, 2)) + (pow(cat_adjacente, 2))))

print("Comprimento da Hipotenusa: {:.2f}".format(hipotenusa))

'''
Versões simplificadas:
hipotenusa = math.hypot(cat_oposto, cat_adjacente)
hipotenusa = (cat_oposto ** 2 + cat_adjacente ** 2) ** (1/2) 
'''