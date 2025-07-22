#Faça um programa em Python que leia um valor inteiro e mostre a tabuada de 1 a 10 do valor lido.

print('\t ----Tabuada----')
numero = int(input('Informe o numero para ver a tabuada: '))

print('\n Tabuada de', numero, ':')

for i in range(1, 11):
	print(numero, 'X', i, '=', (numero * i))