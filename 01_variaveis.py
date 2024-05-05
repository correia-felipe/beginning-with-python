'''
Variáveis
Forma de armazenar variáveis no computador(RAM memory)
Pensemos nesse processo como um armário(ram) com varias gavetas(slot na memória) e nós iremos guardar itens(variáveis) dentro do armário(ram). Para sabermos o onde está cada coisa, definimos nomes nas variáveis.
'''
nome = 'felipe'
idade = 28
altura='1,72'
peso = 98.5
programador = True
rico = False
#armazenei esses dados na memoria. agora o python ja sabe onde ele está e consegue recuperar ele facilmente 

#mostrando os valores definidos nas variaveis
print(nome)
print(idade)
print(altura)
print(peso)
print(programador)
print(rico)

# printando texto com váriaveis previamente declaradas. Podemos escrever um texto e inserir essas infos no texto.
print(f'Olá, {nome}. Vi que vc tem {idade} anos. Com base na sua altura de {altura}cm e peso de {peso}kg, noto que voce está acima do peso.')

##################################################################################################################################################

'''
TIPOS DE DADOS
- **INT** 
        Inteiros
        10,100, -100,-100000000 
- **FLOAT** 
        Números quebrados
        10.5,100.2, -100.100,-100000000.5
- **Strings** 
        Textos, ou qualquer coisa definida dentro de aspas
        'felipe','10', 'celulares'
- **Bool** 
        Verdadeiro ou falso(True ou False)     
'''

print(f'o tipo de dados da variável idade é {type(idade)}')
print('#########################################')
print(f'o tipo de dados da variável nome é {type(nome)}')
print('#########################################')
print(f'o tipo de dados da variável altura é {type(altura)}')
print('#########################################')
print(f'o tipo de dados da variável peso é {type(peso)}')
print('#########################################')
print(f'o tipo de dados da variável programador é {type(programador)}')
