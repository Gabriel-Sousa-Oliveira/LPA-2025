nome_sobrenome = input('Olá, digite o seu nome e sobrenome por favor! ')
print(f'Olá {nome_sobrenome}, Seja bem-vindo ao menu de compras do Gabriel Sousa Oliveira!')

Quantidade = int(input('Digite a quantidade desejada: '))
Valor_Unitario = float(input('Digite o valor unitário: '))

Valor_final = Quantidade * Valor_Unitario

print(f"O Valor final sem desconto é: {Valor_final:.2f}")

if Valor_final != 0:
    if  0 < Valor_final <= 2500:
        print(f'O desconto será de 0% e o valor do seu produto é: R$ {Valor_final:.2f}')
    elif 2500 < Valor_final <= 6000:
        novo_valor = Valor_final * 0.96
        print(f'O desconto será de 4% e o valor final passa a ser: R$ {novo_valor:.2f}')
    elif 6000 < Valor_final <= 10000:
        novo_valor = Valor_final * 0.93
        print(f'O desconto será de 7% e o valor final passa a ser: R$ {novo_valor:.2f}')
    elif 10000 <= Valor_final:
        novo_valor = Valor_final * 0.89
        print(f'O desconto será de 11% e o valor final passa a ser: R$ {novo_valor:.2f}')
else:
    print('O valor final não pode ser zero ou negativo, tente novamente')