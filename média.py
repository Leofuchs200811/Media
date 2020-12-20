# Cria as variáveis total e quantidade
total = 0
quantidade = 0

while True:
    # Cria a variável 
    valor = input("Digite um valor: ")

    if valor == "cancelar" or valor == "c":
        if quantidade > 0:
            break
        print("Conta inválida... Digite pelo menos um valor para poder encerrar o programa.")
        continue

    try:
        total = total + float(valor)
    except ValueError:
        print("Valor inválido. Digite um número válido por favor...")
        continue
    
    if (quantidade + 1) == 5:
        break

    
    quantidade = quantidade + 1
print(total / quantidade)