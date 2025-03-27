def escolha_servico(): # Função para escolher o serviço
    servicos = {
        "DIG": {"Nome": "Digitalização", "Preço": 1.10},
        "ICO": {"Nome": "Impressão Colorida", "Preço": 1.00},
        "IPB": {"Nome": "Impressão Preto e Branco", "Preço": 0.40},
        "FOT": {"Nome": "Fotocópia", "Preço": 0.20}
    }
    while True:
        pedido = input("Por favor, digite a opção desejada [DIG/ICO/IPB/FOT]: ")
        if pedido in servicos:
            return servicos[pedido]["Nome"], servicos[pedido]["Preço"]
        else:
            print("Opção inválida, tente novamente.")

def num_pagina(): # Função para escolher o número de páginas
    while True:
        try:
            paginas = int(input("Digite o número de páginas: ")) # Solicita o número de páginas
            if paginas >= 20000:
                print("Quantidade de páginas excede o limite permitido. Tente novamente.")
            elif paginas >= 2000:
                print("Seu desconto será de 25%. ")
                return paginas * 0.75  # Desconto de 25%  
            elif paginas >= 200:
                print("Seu desconto será de 20%. ")
                return paginas * 0.80  # Desconto de 20%
            elif paginas >= 20:
                print("Seu desconto será de 15%.")
                return paginas * 0.85  # Desconto de 15%
            else:
                print("Pedido sem desconto " )
                return paginas  # Sem desconto
        except ValueError:
            print("Entrada inválida! Digite um número válido.")

def servico_extra():   # Função para escolher o serviço adicional
    extras = {
        "1": {"Nome": "Encadernação Simples", "Preço": 15.00},
        "2": {"Nome": "Encadernação Capa Dura", "Preço": 40.00},
        "0": {"Nome": "Nenhuma das opções", "Preço": 0.00}
    }
    print("1-Encadernação Simples")
    print("2 - Encadernação Capa Dura")
    print("0 -Nenhuma das opções")
    while True:
        extra = input("Escolha um serviço adicional (1/2/0): ")
        if extra in extras: # Verifica se a opção é válida
            return extras[extra]["Nome"], extras[extra]["Preço"]
        else:
            print("Opção inválida, tente novamente.")

# Código principal (main)
print("Olá! Seja bem-vindo ao menu da copiadora do Gabriel Sousa Oliveira!")
nome_sobrenome = input("Digite seu nome e sobrenome: ") # Solicita o nome e sobrenome do cliente
print(f"Olá {nome_sobrenome}, vamos iniciar seu pedido!")
print("DIG - Digitalização - R$1,10 por página")
print("FOT - Fotocópia - R$0,20 por página")
print("IPB - Preto e branco - R$0,40 por página")
print("ICO - Impresão Colorida - R$1,00 por página")

total = 0.0
while True:
    nome_servico, preco_servico = escolha_servico() # Chama a função para escolher o serviço
    num_paginas_com_desconto = num_pagina()     # Chama a função para escolher o número de páginas
    nome_extra, preco_extra = servico_extra()  # Chama a função para escolher o serviço adicional
    
    subtotal = (preco_servico * num_paginas_com_desconto) + preco_extra # Calcula o subtotal
    total += subtotal # Atualiza o total da compra
    
    print(f"Você escolheu {nome_servico}, com {int(num_paginas_com_desconto)} páginas, e adicional {nome_extra}.")
    print(f"Subtotal do item: R$ {subtotal:.2f}")
    print(f"Total acumulado: R$ {total:.2f}")
    
    continuar = input("Deseja adicionar mais itens? (S/N): ") # Pergunta se deseja adicionar mais itens
    if continuar == "N": # Se a resposta for 'N', finaliza a compra
        print(f"\nCompra finalizada. Total a pagar: R$ {total:.2f}")
        print(f"Obrigado, {nome_sobrenome}, por comprar conosco!")
        break # Sai do loop
