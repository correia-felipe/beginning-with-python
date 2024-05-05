'''
FÁCIL 
Construa uma programa que solicite ao usuario inserir nome do produto, como se fosse uma lista de supermercado. Esses valores precisam alimentar um dicionario. Salve o dicionario com todos valores. Pelo menos 10 itens. 
'''
import re
def listinha()-> list: 
    #
    while True:
        resposta = input("Olá! Insira sua lista de supermercado aqui, sem virgulas. Iremos te ajudar a realizar sua compra.: ")
        if re.search(r'\d', resposta):
            print("A resposta contém um caractere numérico!\n")
        else:
            lista_mercado = resposta.strip().split()
            print('\nLista salva!')
            
            break
        return lista_mercado
            
# listinha()

'''
# INTERMEDIÁRIO 
## Crie uma variável com o valor 100. É esse valor que você tem para usar no mercado. Crie um catálogo de produtos, com nome de produto e valores. Pegue a lista pronta e vá ao supermercado. A cada produto comprado vc deve encontrá-lo no catálogo, pegar o valor dele e subtrair da sua carteira. Quando faltar 10 reais pra acabar, vc deve informar ao consumidor que está chegando ao fi. Ao acabar seu saldo, devemos informar ao cliente que nao pode comprar mais. Esse processo deve ser feito por etapas, item a item e sendo printado cálculo por cálculo. 
'''

carteira = 100
lista_mercado = listinha()

catalogo ={'arroz': 5, 'feijao': 3, 'brocolis': 9,'macarrao':13, 'carne': 43,'linguica':20, 'cerveja':42}

for i in lista_mercado:
    custo = catalogo.get(i)
    if custo is not None:
        if carteira >= custo:
            valor = carteira - custo
            carteira = valor
            print(f'Você está comprando {i}, que custa {custo} reais. Agora você tem {valor} reais para continuar comprando.')
            if carteira <= 10:
                print(f'Você só tem {carteira} reais. A grana está acabando.')
        else:
            print(f'Você não tem dinheiro suficiente para comprar {i}!')
    else:
        print(f'O produto {i} não está no catálogo.')
print('Finalizado. Bom dia. :)')