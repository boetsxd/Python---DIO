# Exercício 3: Desenvolva um programa que peça duas notas de um aluno e calcule a média. 
# O programa deve dizer se o aluno foi:
# - Aprovado (média >= 7)
# - Em recuperação (média entre 5 e 6.9)
# - Reprovado (média < 5)

nota1 = float(input("Informe a primeira nota do aluno: "))
nota2 = float(input("Informe a segunda nota do aluno: "))

media = ((nota1 + nota2)/2)

if media >= 7:
    print(f"Aluno aprovado, sua média é: {media}!")
elif  5 < media <= 6.9:
    print(f"Aluno em recuperação, sua média é: {media}!")    
else:
    print(f"Aluno reprovado, sua média é: {media}!")
