altura = float(input("Qual a altura da parede? "))
largura = float(input("Qual a largura da parede? "))

area = altura * largura
litros_tinta = area / 2

print("Área da Parede: {}m² \n Quantidade de tinta necessária: {}l".format(area, litros_tinta)) 