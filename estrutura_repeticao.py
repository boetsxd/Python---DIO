texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

# Exemplo utilizando um iterável
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print() #adiciona uma quebra de linha
    print("Executa no final do loop for")


# Exemplo utilizando a funnção built-in range
for numero in range(0, 51, 5):
    print(numero)


