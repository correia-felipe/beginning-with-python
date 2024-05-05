'''
Laço For e While 
'''
#############
### WHILE ### 
#############

# Enquanto verdadeiro, faça.

n = 0 
while n <=10:
    print(n)
    n += 1
    
'''aqui adicionamos uma variavel(n) e utilizamos ela para dar o start em nosso loop. 
enquanto n for menor ou igual a dez o loop vai printar o valor de N e após isso vai somar 1 no valro de N, ou seja, na primeira
interacao o N vale 0, na segunda, 1 na terceira, 2.... até chegar em 10 e finalizar o loop.
'''
print('########################')
# criando tabuada do 7 
n = 0 
print('\n###TABUADA DO 7###')
while n <=10:
    resultado = n * 7
    print(f'{7} x {n} é igual a {resultado}')
    n += 1
print('#######FINAL#######')


#######
#BREAK#
#######
# criando tabuada do 7 

n = 0 
print('\n###TABUADA DO 7###')
while n <=10:
    if n ==6:
        print('JÁ ERA!')
        break ####################
    resultado = n * 7
    print(f'{7} x {n} é igual a {resultado}')
    n += 1
print('#######FINAL#######')
print('\n#####################################')
print('\n####### LAÇO FOR #######')

#########
## FOR ##
#########

#Para tudo dentro disso, faça isso.

for i in range(0,11): # FOR nao inclui o último valor disposto dentro do range. No caso, ele vai até 10!
    print(i)
    
print('\n\n###TABUADA DO 7###')
for i in range(0,11):
    resultado = i * 7
    print(f'{7} x {i} é igual a {resultado}')

print('#######FINAL#######\n')

print("Pegando apenas números pares de um range de valores")

for i in range(2,20):
    if i % 2 == 0: ## qualquer numero divisível por dois(nao tendo resto) é par.
        print(f'{i} é par!')

print("\n\nPegando apenas números pares de um range de valores - jeito Pythonico")        
for i in range(2,20,2): # aqui adicionamos o passo que ele deve dar em cada etapa. No caso, ele irá iterar a cada dois passos, ou seja, comecando no zero só trazendo os pares.
    print(f'{i} é par!')
    
print("\n\nagora gerando a tabuada do 1 ao 10")
for i in range(1,11):
    print(f'\n###TABUADA DO {i}!###\n')
    for j in range(1,11):
        resultado = i * j
        print(f'{i} x {j} é igual a {resultado}')