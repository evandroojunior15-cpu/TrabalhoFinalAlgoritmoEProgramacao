nome = input("Digite seu nome: ")

valor_total = 0.0
continuar_pedido = True

while continuar_pedido:

    print("---- Cardápio ----")
    print("NOME                CÓDIGO   PREÇO")
    print("Pastel                1      12.00")
    print("Caldo de cana         2       6.00")
    print("Coxinha               3       7.00")
    print("Cigarrete             4       6.00")
    print("Refrigerante          5       5.00")
    print("Finalizar pedido      0")

    codigo = int(input("Digite o código do produto: "))

    match codigo:
        case 0:
            continuar_pedido = False
        case 1:
            preco = 12.00
        case 2:
            preco = 6.00
        case 3:
            preco = 7.00
        case 4:
            preco = 6.00
        case 5:
            preco = 5.00
        case _:
          preco = 0.0
          print("Opção Inválida!")

      # só pede quantidade e calcula se o código for de um produto válido (1 a 5)
    if codigo != 0 and 1 <= codigo <= 5:
        quantidade = int(input("Digite a quantidade:"))

        if quantidade <=0:
            print("Quantidade Inválida!")
        else:
            subtotal = preco * quantidade
            valor_total+= subtotal
            print(f"Subtotal: R$ {subtotal:.2f}")
            print(f"Total acumulado: R${valor_total:.2f}")


# calculo do desconto

if valor_total < 50.00:
    percentual_desconto = 0
elif valor_total <= 99.99:
    percentual_desconto = 5
else:
    percentual_desconto = 10

valor_desconto = valor_total * (percentual_desconto / 100)
valor_final = valor_total - valor_desconto

#forma de pagamento

pagamento_valido = False

while not pagamento_valido: #o not inverte o valor de um booleano
    opcao_pagamento = int(input("\nForma de pagamento:\n1 - Dinheiro\n2 - PIX\n3 - Cartão\nOpção:"))

#

    match opcao_pagamento:
        case 1:
            forma_pagamento = "Dinheiro"
            pagamento_valido = True
        case 2:
            forma_pagamento = "PIX"
            pagamento_valido = True
        case 3:
            forma_pagamento = "Cartão"
            pagamento_valido = True
        case _:
            print("Opção de pagamento inválida. Tente novamente.")


## final

print("\n---- Resumo do pedido ----")
print("Cliente:", nome)
print(f"Valor original: R$ {valor_total:.2f}")
print(f"Desconto aplicado: {valor_desconto}%")
print(f"Valor final: R$ {valor_final:.2f}")
print("Forma de pagamento:", forma_pagamento)
