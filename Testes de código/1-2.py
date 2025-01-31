# Exercício 2: Crie um programa que pergunte a idade do usuário e diga em qual categoria ele se encaixa:
# - Menor de 18 anos: Menor de idade
# - Entre 18 e 60 anos: Adulto
# - Acima de 60 anos: Idoso

idade = int(input("Informe sua idade: "))
if idade < 18:
    print("Você é classificado como: Menor de idade")
elif 18 <= idade <= 60:
    print("Você é classificado como: Adulto")
else:
    print("Você é classificado como: Idoso")