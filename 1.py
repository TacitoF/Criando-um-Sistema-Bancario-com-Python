from datetime import datetime, timedelta

saldo = 0
resposta = 0
deposito = 0
extrato = ""

while True:

    resposta = int(input("Digite uma das opções\n"
    "1- Deposito\n" \
    "2- Saque\n" \
    "3- Extrato\n" \
    "4- Sair\n" \
    "Insira uma opção: "))
    print("")

    if resposta == 1:
         deposito = int(input("Digite o valor a ser depositado: "))
         print("")
         if deposito > 0:
           saldo += deposito
           extrato += f"Deposito de R${deposito}\n"
           print(f"Seu deposito de R${deposito} foi concluido com sucesso\n")
         else:
            print("Valor inválido!\n")

    elif resposta == 2:
        total_saque = 0
        saque = int(input("Digite um valor a ser sacado: "))
        print("")
        if total_saque > 3:
            print("Limite de saques diários atingido!\n")
        
        elif saque > 500:
            print("O limite de Valor de saque foi excedido!\n")
        
        elif saque <= 0:
            print("Valor Inválido!\n")
        
        else:
            total_saque += 1
            saldo -= saque
            print(f"Seu saque de {saque} foi realizado com sucesso!\n")
            extrato += f"Saque de R${saque}"

    elif resposta == 3:
        print("========== Extrato ==========")
        print("Nenhum movimento na conta" if not extrato else extrato)
        print(f"Saldo: {saldo}")
        print("=============================\n")
    elif resposta == 4:
        print("Saindo...")
        break
    else:
        print("opção invalida! Digite uma opção válida\n")