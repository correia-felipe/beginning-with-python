'''
## Dicionários
- Lista -> Acessada através de posição ou índice
- Dicionário -> Acessado através de uma chave.
- Dicionário armazena dados sem ordenação. Para acessar um item, nao precisamos se ater a algum tipo deindex, basta sabermos a chave de busca que encontraremos o solicitado.
##               {chave1: valor1, chave2: valor2}
'''

lista_telef = {"felipe": 967732088, "lari": 985647605}

tel_felipe = lista_telef["felipe"]
print(tel_felipe)

print('\nadicionando itens ao dicionario') 
lista_telef['victor'] = 874459624
print(lista_telef)

print(f'\nexcluir algum item do dicionario com base na chave') 
lista_telef.pop('felipe')
print(lista_telef)


print('\njuntando dois dicionarios -  Caso já exista a chave, o valor será alterado para o que estamos atualizando')
endereço = {'rua borges': 'parada inglesa', 'servidao':'sao joao'}
lista_telef.update(endereço)
print(lista_telef)

print('\blista com as chaves presentes no dicionario') 
print(lista_telef.keys())

print('\nlista com os valores presentes no dicionario') 
print(lista_telef.values())

print('\ntupla com os pares de chave-valor presentes no dicionario') 
print(lista_telef.items())

print('\nverificar bool se existe a chave dentro do dicionario') 
print('lari' in lista_telef)

print('\nfatiando a chave em outros dicionarios. Se nao especificar, None virá padrão no valor')
print(lista_telef.fromkeys('lari',3))

print('\ncopiando a lista para nova lista')
lista2 = lista_telef.copy()
print(lista2)

print('\nremovendo todos itens do dicionario')
lista2.clear()
print(lista2)

print('\npegando o valor da chave sem causar erro caso nao exista. Se valor nao especificado, vem como None. Falaremos mais a frente')
print(lista_telef.get('lari'))

print("\ntransformando dicionario em uma lista") 
lista3 = lista_telef.items() 
print(lista3)

print("\n##############################################")
print("############# METODO MAGICO ##################")
print("##############################################")
print('\n__ getitem __')
print('\nesse método é muito útil, pois inibe retornos de erros em falta de chaves. Sua estrutura é:')
print('dicionario.get("CHAVE")')

dicionario = {'nome':'felipe','end':'rua borges'}
print(dicionario)
print('\nBuscando dados em uma chave existente')
print(dicionario['end'])
print('\nbuscando dados em uma chave que não existe SEM O METODO MAGICO')
#dicionario['idade']
print('Nos retorna um erro de chave, pois nao encontrou essa chave. Com isto nosso codigo irá "quebrar" toda vez que nao encontrar. Em casos como esse o método GET nos apoia. Inibe nosso codigo que trazer erro.')
print('\nBuscando dados existentes com o GET')
print(dicionario.get('nome'))
print("\nBuscando chave que não existe com o GET.") 
print(dicionario.get('idade'))
print('\nCom isto nosso codigo nao retorna erro. Retorna um valor default.\n')
tel_lari = lista_telef.get("lari")
print(tel_lari)

print("\n##############################################")
print("############# ITERANDO ##################")
print("##############################################")

print('__ items __')
print('\nConseguimos coletar dados dentro de um dicionário e transformá-lo em um iterável(lista) para podermos fazer diversas operações.')
pessoa = {'nome':'felipe','sobrenome':'correia'}
print('\nprintando todo o dicionário. Ele virá em forma de lista, com cada chave-valor correpondente dentro de sua tupla.')
print(pessoa.items())
print('\niterando sobre o dicionario')
for i,j in pessoa.items():
    print(f'chave: {i}, valor: {j}')