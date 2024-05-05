'''
Funções
 Blocos de código que executam uma função específica. 
 - Inibe a necessidade de ficar escrevendo várias vezes o mesmo código. 

'''
print('### primeira funcao ###\n')
def funcao(): 
    print("Bloco de código")

funcao()
print('\nRecebendo e retornando dados.')
def informa_nome(nome, cidade):
    return print(f'Olá, {nome} de {cidade}. Seja bem vindo.')

informa_nome('felipe','sp')
informa_nome('larissa','rj')
informa_nome('cooper','ny')

print('sem inserir parametros onde deveria receber parametro -RETORNA ERRO')
#informa_nome()

print('\nFuncoes com parametros pre definidos para retornar um valor porem quando nomeados esses parametros ele se altera conforme definimos.')
def flores(flor='margarida',cor='amarela'):
    return print(f' a flor {flor} é da cor {cor}.')
print('\nDeixando padrao') 
flores()

print('\nDefinindo novos parametros') 
flores('azaléa','azul')

print("############")
print("### ARGS ###")
print("############")
print('Caso você queira que a função receba um valor variável de parâmetros, podemos passar *args, e quando formos definir os parâmetros, podemos passá-los em tupla.')

def pares(*args):
    for num in args:
        if num % 2 == 0:
            print(f'{num} é par!!')
        else:
            print(f'{num} é impar!')


pares(23,44,57,90,88)
print("##############")
print("### KWARGS ###")
print("##############")
print('Se quisermos desenvolver uma função com número variado de parâmetros nomeados, utilizaremos **kwargs. Os valores serão guardados em formato de um dicionário.\n')


def usuario(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")


usuario(nome='felipe', idade=28, carreira='Engenheiro de Dados')

print('funcao retornando um dado.')
def soma(a,b):
    return a + b

resultado = soma(2,5)
print(resultado)

print('\nfuncao retornando multiplos dados')
def somaMedia(a,b):
    return a + b, (a+b)/2

soma, media = somaMedia(2,5)
print(soma)
print(media)
