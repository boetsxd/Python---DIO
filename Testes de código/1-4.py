# Exercício 4: Escreva um programa que peça ao usuário um número e verifique:
# - Se é positivo, negativo ou zero.
# - Se é par ou ímpar.

numero = int(input("Informe um número: "))

if numero > 0:
    if (numero % 2 == 0):
        print("Este número é positivo e par")
    else:
        print("Este número é positivo e ímpar")
elif numero < 0:
    if (numero % 2 == 0):
        print("Este número é negativo e par")
    else:
        print("Este número é negativo e ímpar")
else:
    print("Este número é zero")
    
# Outra solução simplificada:
# numero = int(input("Informe um número: "))
# 
# if numero > 0:
#     impoupar = "par" if (numero % 2 == 0) else "ímpar"
#     print(f"Este número é positivo e {par_ou_impar}")
# elif numero < 0:
#     impoupar = "par" if (numero % 2 == 0) else "ímpar"
#     print(f"Este número é negativo e {par_ou_impar}")
# else:
#     print("Este número é zero")
