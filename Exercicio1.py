nome_sobrenome = input('Olá, digite o seu nome e sobrenome por favor! ') #Pede ao Usuário sua idenfiticação ( nome e sobrenome))
print(f'Olá {nome_sobrenome}, Seja bem-vindo ao menu de compras do Gabriel Sousa Oliveira!') #Mostra ao usuário uma mensagem de boas vindas

Quantidade = int(input('Digite a quantidade desejada: ')) #Pede ao usuário a quantidade desejada
Valor_Unitario = float(input('Digite o valor unitário: ')) #Pede ao usuário o valor unitário

Valor_final = Quantidade * Valor_Unitario #Calcula o valor final

print(f"O Valor final sem desconto é: {Valor_final:.2f}") #Mostra o valor final sem desconto

if Valor_final != 0:
    if  0 < Valor_final <= 2500:
        print(f'O desconto será de 0% e o valor do seu produto é: R$ {Valor_final:.2f}')
    elif 2500 < Valor_final <= 6000:
        novo_valor = Valor_final * 0.96 #Calcula o novo valor com desconto de 4%
        print(f'O desconto será de 4% e o valor final passa a ser: R$ {novo_valor:.2f}')
    elif 6000 < Valor_final <= 10000:
        novo_valor = Valor_final * 0.93 #Calcula o novo valor com desconto de 7%
        print(f'O desconto será de 7% e o valor final passa a ser: R$ {novo_valor:.2f}')
    elif 10000 <= Valor_final:
        novo_valor = Valor_final * 0.89 #Calcula o novo valor com desconto de 11%
        print(f'O desconto será de 11% e o valor final passa a ser: R$ {novo_valor:.2f}')
else:
    print('O valor final não pode ser zero ou negativo, tente novamente')   #indica que o valor final não pode ser zero ou negativo
print('Obrigado por comprar conosco, volte sempre!') 
