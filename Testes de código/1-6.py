# Exercício 6: Escreva um programa que use os operadores de comparação para verificar:
# - Se dois números fornecidos pelo usuário são iguais.
# - Se o primeiro é maior ou menor que o segundo.

num1 = int(input("Informe o primeiro número: "))
num2 = int(input("Informe o segundo número: "))

if num1 != num2:
    compare = "maior" if num1 > num2 else "menor"
    print(f"Estes números são diferentes e {num1} é {compare} que {num2}")
else:
    print(f"Estes números são iguais")
