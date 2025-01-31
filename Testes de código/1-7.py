# Exercício 7: Desenvolva um programa para verificar se uma palavra fornecida pelo usuário está em 
# uma frase específica. Use operadores de associação (in e not in).


frase = "A rua estava calma, mas a noite estava escura."

palavra = input("Digite uma palavra: ")

if palavra.lower() in frase.lower():
    print(f"A palavra '{palavra}' está na frase.")
else:
    print(f"A palavra '{palavra}' não está na frase.")