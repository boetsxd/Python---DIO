conta_normal  = True
conta_universitaria = False
conta_especial = True

saldo = 2000
saque = 2500
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print("Saque efetuado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque efetuado com uso do cheque especial!")
    else:
        print("Não foi possível realizar o saque, saldo insuficiente!")

elif conta_universitaria:

    if saldo >= saque:
        print("Saque efetuado com sucesso!")
    else:
        print("Saldo insuficiente!")

elif conta_especial:
    print("Conta especial selecionada!")

else:
    print("Sistema não reconhece o tipo de conta, entre em contato com o gerente!")