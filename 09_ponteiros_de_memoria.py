'''
## Ponteiro de Memória 
Qualquer variável ou estrutura de dados que é criada em Python, se é alocado um endereço de memória para armazenamento com um endereço único. <br>
Em casos de variáveis nós temos um ponteiro direto apontando para o endereço de memória onde foi gravado o registro. <br>
Em casos de estrutura de dados não temos esse endereço direto, e sim uma referência para o endereço. Abaixo veremos mais sobre.
'''

print('criando uam variável e verificando onde ela está.Iremos usar uma funcao propria do python para encontrar o local e retornar o valor em hexadecimal.')
x = 42
print(x)
print(hex(id(x)))

print("\ncriando uma variável nova com base na variável anterior. Enquanto são iguais, a mais nova fica apenas um espelho da antiga.")
y = x 
print(y)
print(hex(id(y)))
print('\n alterando a nova e ver como ela se comportará')
y = 40 
print(y)
print(hex(id(y)))
print('Ela alterou seu endereço de memória para um novo.') 
print('\nveremos como a antiga está') 
print(x)
print(hex(id(x)))
print('A antiga continuou com o mesmo endereço. Então podemos concluir que em casos de variáveis elas são independentes quando alteradas. Até a variável de referência, quando alterada não remete na nova.') 
print('\n#####################################')
print('\nQuando se trata de estruturas de dados, isso é um pouco diferente. O endereço de memória é apontado, entao qualquer alteração na nova/antiga estrutura irá remeter em todos referenciados.') 

print ('criando  lista')
old = ['felipe','correia']
print(old)
print(hex(id(old)))
print('\ncriando uma nova lista a partir de outra')
new = old 
print(hex(id(new)))
print('Acima os valores de endereço de memória são iguais.')
print('\nIremos agora adicionar um item na lista de referencia')
old.append('28 anos')
print(old)
print(hex(id(old)))
print('\nprintando nova lista') 
print(new)
print(hex(id(new)))
print('Acima a lista mais nova adicionou o item adicionado na lista antiga, e ambas se mantiveram com mesmo endereço.')
print('\nAgora iremos adicionar um item na nova.')
new.append('engenheiro')
print(new)
print(hex(id(new)))
print('\nVeremos como se comportou a lista antiga') 
print(old)
print(hex(id(old)))
print('A antiga também se alterou. Isso torna as duas reféns uma da outra. Trazendo ao mundo real, a lista "old" poderia ser o dado como ele veio, e criamos uma nova lista com os dados presentes nela para que no fim da análise possamos juntá-las e fazer um depara. Seguindo essa linha não seria possível. Para contornar isso, é recomendável fazer um .copy() dessa lista, pois aí sim estamos falando ao interpretador Python que é pra ele pegar os dados do endereco "old" e salvar em um novo endereço. vejamos:')
new2 = old.copy()
print(new2)
print('\nrelembremos onde a old está e comparamos com as novas')
print(f'lista OLD {hex(id(old))}')
print(f'lista NEW {hex(id(new))}')
print(f'lista NEW2 {hex(id(new2))}')
print('\nAs duas primeiras estão no mesmo local, e apenas a ultima está emseu devido lugar inidividual. Como ultimo teste, vamos alterar a nova lista e ver se respaldou na antiga.')
new2.append("dados")
print(old)
print(new)
print(new2)print(new2)
