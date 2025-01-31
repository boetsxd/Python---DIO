# Exercício 8: Crie um programa que use operadores lógicos para verificar:
# Se um número fornecido está entre 10 e 20 (inclusive).
# Se é divisível por 3 e por 5.


numero = int(input("Digite um número: "))

if numero in range(10, 21):
    print(f"O número {numero} está entre 10 e 20.")
else:
    print(f"O número {numero} não está entre 10 e 20.")
if numero % 3 == 0 and numero % 5 == 0:
    print(f"O número {numero} é divisível por 3 e por 5.") 
else: 
    print(f"O número {numero} não é divisível por 3 e por 5.")

    