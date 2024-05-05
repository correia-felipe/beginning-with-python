'''
Tuplas
- Imutáveis - NAO SE PODE ALTERAR ITENS DENTRO DA MESMA. Pensemos por exemplo latitude e longitutde de SP. Ela nunca vai mudar.
- Armazenamento persistente 
          (item1, item2)
'''

local = ([-19.0000,90.88888])
print(f'{type(local)}')
print(local)
print(f'\no tamanho dessa tupla é de {len(local)} itens')
print('\nadicionando uma nova lista dentro da tupla existente - ESSA NOVA LISTA É UM NOVO ITEM NA TUPLA')
lugar = ['sao paulo','zn',0]
local.append(lugar)
print(f'{local}')
