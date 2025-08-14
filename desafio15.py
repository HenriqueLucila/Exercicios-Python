dias = int(input("Por quantos dias o carro foi alugado? "))
km = float(input("Quantos kilometros foram percorridos? "))

total = (60 * dias) + (0.15 * km)

print("Total a pagar: R${:.2f}".format(total))