# Faça um programa que receba um número digitado pelo usuário e calcule a soma de todos os números de 1 até ao número digitado. 
# Por exemplo, se o usuário digitou o número 4, a saída deve ser 10 (1+2+3+4=10).

soma_numeros = 0

numero = int(input("Por favor, insira um numero: "))
for i in range(1, numero + 1, 1):
	soma_numeros += i
print("A soma é = ", soma_numeros)