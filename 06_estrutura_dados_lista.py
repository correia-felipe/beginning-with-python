'''
Armazenamento de dados de forma sequencial através de indices.

- Coleções de dados que abordaremos
    - Lista

Mutável - PODEMOS ALTERAR VALORES ANTERIORMENTE DECLARADOS.
Agrega várias variáveis dentro de uma só. PODEMOS TER INT, STRING, TUDO JUNTO.
'''
cores = ['azul','amarelo','verde']
cores

("\nsaber quantos itens tem dentro da lista")
len(cores)

print('\niterando sobre a lista(fazendo alguma operacao com cada item da lista. No caso imprimindo cada um)')
for i in cores:
    print(i)

print('\nBuscando na lista pelo indice - INDICE É A POSICAO DELA. O NUMERO ZERO É O PRIMEIRO ITEM')
print(cores[0])
print(cores[1])
print('\nBuscando na lista pelo indice - ULTIMO ITEM')
print(cores[-1])
print('\nBuscando na lista pelo indice - DENTRO DE UM VALOR DE INDICE. NESSE CASO NAO TRARÁ O ULTIMO INDICE')
print(cores[2:5])

print('\nadicionando mais um iten na lista, ao final dela')
cores.append('preto')
print(cores)

print('\nadicionando um item e informando o indice que ele deve ficar') 
cores.insert(4,'marrom')
print(len(cores))
print(cores)

print('\nremovendo um item especifico')
cores.remove('amarelo')
print(cores)

print('\nexcluindo o ultimo item da lista') 
cores.pop()
print(cores)

print('\njuntando duas listas em uma')
neutros = ['cinza','bege','lilás']
cores.extend(neutros)
print(cores)

print('\npercorrendo indices de uma lista') 
for i,j in enumerate(cores): # nao se preocupar com o enumerate agora. Mais a frente veremos
    print(f'A cor {j} está no index {i}')
    
print("\ncriando uma nova lista pegando itens de outra lista através de um filtro")
lista_filtrada = [x for x in cores if x in 'preto']
lista_filtrada

print("\ncriando uma lista utilizando um range de valores pares")
lista_num = list(range(0,22,2))
print(lista_num)