

nome_sobrenome = input('Olá, digite o seu nome e sobrenome por favor! ')
print(f'Olá {nome_sobrenome}, Seja bem-vindo ao menu de compras da loja de açai e cupuaçu do Gabriel Sousa Oliveira!')

Sabores = {
"AC" :  ['Açai'],
"CP":  ['Cupuaçu']
}
Sabor = input("Por favor digite o Sabor (AC/AP): ")
if Sabor in Sabores:
    print(f"Ótima escolha! {Sabor} está disponível. ")
else:
    print("Desculpe, esse sabor não está disponível, tente novamente ")

Tamanhos = {
 "P" : ['Pequeno'],
"M" : ['Médio'],
"G" : ['Grande']
}
Tamanho = input("Por favor, Digite o tamanho desejado (P/M/G)")
if Tamanho in Tamanhos:
    print(f'Você escolheu o tamanho {Tamanho} ')
else:
    print(" o tamanho digitado é invalido")