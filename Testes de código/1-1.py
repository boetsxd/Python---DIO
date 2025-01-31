# Exercício 1: Crie um programa que peça ao usuário para inserir três números. Em seguida:
# - Converta um deles para um número inteiro, outro para um número decimal e outro para uma string.
# - Exiba os valores convertidos junto com seus tipos.

numero_1 = int(input("Informe o primeiro número: "))
print(f"O número digitado é {numero_1}, seu tipo é {type(numero_1)}")

numero_2 = float(input("Informe o segundo número: "))
print(f"O número digitado é {numero_2}, seu tipo é {type(numero_2)}")

numero_3 = input("Informe o terceiro número: ")
print(f"O número digitado é {numero_3}, seu tipo é {type(numero_3)}")
