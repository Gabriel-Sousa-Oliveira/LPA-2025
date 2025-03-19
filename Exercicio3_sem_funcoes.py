nome_sobrenome = input('Olá, digite o seu nome e sobrenome por favor! ')
print(f'Olá {nome_sobrenome}, Seja bem-vindo ao menu de compras da loja de açai e cupuaçu do Gabriel Sousa Oliveira!')

servico = {
    "DIG" : {"Nome" :"Digitalização" , "Preço":  0.10},
    "ICO":  {"Nome":"Impresão Colorida", "Preço": 1.00} ,
    "IPB" : {"Nome":"Preto e branco",  "Preço": 0.40},
    "FOT": {"Nome":"Fotocópia", "Preço": 0.20} 
}

Extras = {
    "1" : {"Nome" :"Encadernação Simples" , "Preço":  15.00},
    "2" : {"Nome" :"Encadernação capa dura" , "Preço":  40.00},
    "0" : {"Nome" :"Nenhuma das opções" , "Preço":  0.00}
}
total = 0.0 
while True:
    
    while True:
        Pedido = input("Por favor digite a opção desejada [DIG/ICO/IPB/FOT] ou Digite 'Cancelar' para encerrar a operação:")

        if Pedido == 'Cancelar':
            print("Pedido Cancelado")
            break
    
        if Pedido in servico:
            nome_pedido = servico[Pedido]["Nome"]  
            preco_pedido = servico[Pedido]["Preço"]
            preco_pedido = float (preco_pedido)
            total += preco_pedido
            break
        else:
         print(f"Desculpe, esse sabor não está disponível, tente novamente ")

    print(f" Boa escolha, {nome_pedido} esta disponivel")
    
    num_paginas = input(f"Por favor  digite o numero de paginas:")
    num_paginas = int (num_paginas)
    
    while True:
        Extra = input("Por favor, Digite o Serviço adicional desejado (1/2/0) ou Digite 'Cancelar' para encerrar a operação")

        if Extra == 'Cancelar':
            print("Pedido Cancelado")
            break          
    
        if Extra in Extras:
            nome_Adicoional = Extras[Extra]["Nome"]
            preco_Adicoional = Extras[Extra]["Preço"]
            preco_Adicoional = float (preco_Adicoional)

            print(f'Você escolheu adicionar {nome_Adicoional} ')
            break
        else:
            print(" o tamanho digitado é invalido")
        
    
    total = (preco_pedido * num_paginas) + preco_Adicoional

    

# Exibe os detalhes do pedido
    print(f" {nome_pedido} {nome_Adicoional} adicionado ao pedido! Preço: R$ {total:.2f}")
    print(f"Total atual da compra: R$ {total:.2f}")

    continuar = input("\nDeseja adicionar mais itens? (S/N): ").strip().upper()
    if continuar == "N":
        print("\n Compra finalizada.")
        print(f"Total da compra: R$ {total:.2f}")
        print(f"Obrigado {nome_sobrenome} por comprar conosco! ")
        break



    print("Escolha um serviço:")
print("DIG - Digitalização")
print("FOT - Fotocópia")
print("IPB - Preto e branco")
print("ICO - Impresão Colorida")