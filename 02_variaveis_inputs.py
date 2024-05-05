
'''
Solicitando dados ao usuário e realizando operações com esses dados(inputs = entradas)

Ideal elencar o tipo de dado que irá receber, para que possa utilizá-lo em operacoes que so aceitam numeros
'''

nome = input('Seja bem vindo(a) a nossa calculadora de IMC. Para começar,qual seu nome?: ')
idade = input("E sua idade?: ")
altura = float(input('Qual altura?: '))
peso = float(input('Por último, seu peso:'))
#
imc = round(peso / altura ** 2,2)

#
if imc >= 30:
    print(f'Olá, {nome}. Vi que vc tem {idade} anos. Com base na sua altura de {altura}cm e peso de {peso}kg, noto que voce está com imc de {imc}, ou seja, acima do peso.')
else:
    print(f'Olá, {nome}. Vi que vc tem {idade} anos. Com base na sua altura de {altura}cm e peso de {peso}kg, noto que voce está com imc dentro do padrão.')
