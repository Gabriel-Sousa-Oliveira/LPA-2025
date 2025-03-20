nome_sobrenome = input('Olá, digite o seu nome e sobrenome por favor! ') # Solicita o nome e sobrenome do cliente
print(f'Olá {nome_sobrenome}, Seja bem-vindo ao menu de compras da loja de açai e cupuaçu do Gabriel Sousa Oliveira!')

Sabores = {
"AC" :  "Açai",
"CP":  "Cupuaçu"
}  # Dicionário com os sabores disponíveis
Tamanhos = {
    "P": "Pequeno",
    "M": "Médio",
    "G": "Grande"
} # Dicionário com os tamanhos disponíveis
precos = {
    "Pequeno": {"CP": 9, "AC": 11},
    "Médio": {"CP": 14, "AC": 16},
    "Grande": {"CP": 18, "AC": 20}
} # Dicionário com os preços dos itens
total = 0.0
while True:
    
    while True:
        Sabor = input("Por favor digite o Sabor [AC/CP] ou Digite 'Cancelar' para encerrar a operação:") # Solicita o sabor desejado

        if Sabor == 'Cancelar':
            print("Pedido Cancelado")
            break
    
        if Sabor in Sabores: # Verifica se o sabor é válido
            nome_sabor = Sabores[Sabor]
            break
        else:
         print(f"Desculpe, esse sabor não está disponível, tente novamente ") 

    print(f" Boa escolha, {nome_sabor} esta disponivel") # Exibe o sabor escolhido
    
    
    while True:
        Tamanho = input("Por favor, Digite o tamanho desejado (P/M/G) ou Digite 'Cancelar' para encerrar a operação") # Solicita o tamanho desejado

        if Tamanho == 'Cancelar':
            print("Pedido Cancelado")
            break          
    
        if Tamanho in Tamanhos: # Verifica se o tamanho é válido
            nome_tamanho = Tamanhos[Tamanho]
            print(f'Você escolheu o tamanho {nome_tamanho} ') # Exibe o tamanho escolhido
            break
        else:
            print(" o tamanho digitado é invalido")   
        
    preco_item = precos[nome_tamanho][Sabor]
    total += preco_item # Atualiza o total da compra

# Exibe os detalhes do pedido
    print(f" {nome_sabor} {nome_tamanho} adicionado ao pedido! Preço: R$ {total:.2f}")
    print(f"Total atual da compra: R$ {total:.2f}")

    continuar = input("\nDeseja adicionar mais itens? (S/N): ").strip().upper() # Pergunta se deseja adicionar mais itens
    if continuar == "N":
        print("\n Compra finalizada.")
        print(f"Total da compra: R$ {total:.2f}")
        print(f"Obrigado {nome_sobrenome} por comprar conosco! ")
        break # Encerra o loop