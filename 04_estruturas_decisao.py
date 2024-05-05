'''
- IF 
    SE 
- ELIF
    SE ENTAO 
- ELSE 
    SE NAO 
    
'''

aluno = input('Olá, seja bem vindo a sua secretaria online. Qual seu nome?: ')
num = int(input('digite sua nota do 1tri: '))
num1 = int(input('digite sua nota do 2tri: '))
num2 = int(input('digite sua nota do 3tri: '))
num3 = int(input('digite sua nota do 4tri: '))
#
passar = 7
recup = 4
#
mean = round((num + num1 + num2 + num3) / 4,2)

#
if mean >= passar:
    print(f'Parabéns, {aluno}! Você passou de ano. Sua média anual foi de {mean}.')
elif mean <= recup < passar:
    print(f'{aluno}, você não reprovou mas ficou em recuperacao. Sua média anual foi de {mean}.')
else:
    print(f'Que triste, {aluno}! voce reprovou. Sua media ficou abaixo do comum, com o valor de {mean}.')