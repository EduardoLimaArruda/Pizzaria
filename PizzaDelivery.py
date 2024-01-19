print("Bem-vindo ao Wacky Pizzaria\n")

Sabor = input("Qual o sabor que voce gostaria? Mussarela, Calabresa, Frango, Chocolate ou Meio a Meio?\n")
tamanho = input("\nQual o tamanho da pizza que deseja? Broto, Grande ou Familia\n")

Conta = 0

if Sabor == "Meio a Meio":
    Meio = input("E qual seriam esses sabores? Nós temos: Mussarela e Calabresa, Mussarela e Frango, Calabresa + Frango, Salgado com Doce\n")
    if Meio == "Mussarela e Calabresa":
        Conta += 10.99
    if Meio == "Mussarela e Frango":
        Conta += 10.49
    if Meio == "Calabresa + Frango":
        Conta += 11.49
    if Meio == "Salgado com Doce":
        Meia = input("Qual sabor de salgado você gostaria? Mussarela, Frango ou Calabresa?\n")
        if Meia == "Mussarela":
            Conta += 15.9
        if Meia == "Frango":
            Conta += 15.9
        if Meia == "Calabresa":
            Conta += 15.9
if Sabor == "Mussarela":
    Conta += 9.99
if Sabor == "Calabresa":
    Conta += 11.99
if Sabor == "Frango":
    Conta += 10.99
if Sabor == "Chocolate":
    Conta += 12.99

if tamanho == "Broto":
    Conta += 35
elif tamanho == "Grande":
    Conta += 50
else:
    Conta += 64.5

calabresa = input("\nGostaria de adicionar calabresa? Sim ou Não\n")
queijo = input("\nGostaria de queijo extra? Sim ou Não\n")
borda = input("\nGostaria de borda recheada? Sim ou Não\n")

if calabresa == "Sim":
    Conta += 5.9

if queijo == "Sim":
    Conta += 4.9

if borda == "Sim":
    borda1 = input("\nQual borda você gostaria? Chocolate, Catupiry ou Cheddar\n")
    if borda1 == "Chocolate":
        Conta += 6
    elif borda1 == "Catupiry" or "Cheddar":
        Conta += 5

frete = input("\nSerá para retirar no local ou para entrega? Local ou Entrega?\n")

if frete == "Entrega":
    Conta += 6.9
    endereço = input("\nQual o seu endereço?\n")
    pagamento = input(f"\nO valor final é {round(Conta,2)} reais. Qual a forma de pagamento? Cartao ou Dinheiro?\n")
    if pagamento == "Cartao":
        print(f"\nOk, o motoboy levará a maquininha para o endereço:\n{endereço}.\nMuito obrigado!")
    if pagamento == "Dinheiro":
        troco = float(input("\nSerá necessário troco? Se sim, quanto de troco?\n"))
        if troco < Conta :
            print("\nValor de troco inválido, refaça o pedido")
        else:
            troco -= Conta
            print(f"\nO motoboy levará o troco de {round(troco,2)} reais para o endereço:\n{endereço}.\nMuito obrigado!")
else: 
    print(f"\nCerto, o valor final é {round(Conta,2)} reais. A pizza ficará pronta em 40 minutos.")

enter = input("\nAperte Enter para fechar")