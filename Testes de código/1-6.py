# Exercício 6: Escreva um programa que use os operadores de comparação para verificar:
# - Se dois números fornecidos pelo usuário são iguais.
# - Se o primeiro é maior ou menor que o segundo.

try:
    num1 = int(input("Informe o primeiro número: "))
    num2 = int(input("Informe o segundo número: "))

    if num1 != num2:
        compare = "maior" if num1 > num2 else "menor"
        print(f"Os números são diferentes: {num1} é {compare} que {num2}")
    else:
        print(f"Os números são iguais!")
except ValueError:
    print("Por favor, informe apenas números inteiros")
