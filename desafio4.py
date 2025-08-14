n = input('Digite um valor: ')

print('Tipo primitivo da variável: ', type(n))
print('O valor digitado é um número? ', n.isnumeric())
print('O valor digitado é uma letra? ', n.isalpha())
print('O valor digitado é alfanumérico? ', n.isalnum())
print('O valor digitado está somente com letras maiúsculas? ', n.isupper())
print('O valor digitado está somente com letras minúsculas? ', n.islower())
print('O valor digitado é um espaço em branco? ', n.isspace())

print('O valor digitado foi "{}".'.format(n))
