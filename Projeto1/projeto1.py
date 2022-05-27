from audioop import reverse
import json
import os.path
from sre_constants import CATEGORY_UNI_SPACE
import sys
import pprint

def obter_dados():
    '''
    Essa função carrega os dados dos produtos e retorna uma lista de dicionários, onde cada dicionário representa um produto.
    NÃO MODIFIQUE essa função.
    '''
    with open(os.path.join(sys.path[0], 'dados.json'), 'r') as arq:
        dados = json.loads(arq.read())
    return dados


def listar_categorias(dados) -> set:#
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    Essa função deverá retornar uma lista contendo todas as categorias dos diferentes produtos.
    Cuidado para não retornar categorias repetidas.    
    '''    
    lista_cat = []
    
    for i in range(len(dados)):
        lista_cat.append(dados[i]["categoria"])
    
    lista_cat = set(lista_cat)
    
    return lista_cat

    
def listar_por_categoria(dados, categoria: str) -> list:
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    O parâmetro "categoria" é uma string contendo o nome de uma categoria.
    Essa função deverá retornar uma lista contendo todos os produtos pertencentes à categoria dada.
    '''
    lista_por_cat = []

    for i in range(len(dados)):
        if dados[i]["categoria"] == categoria:
            lista_por_cat.append(dados[i])   

    if lista_por_cat != []:
        return lista_por_cat
    else: return 'Ops... categoria inválida!'
    

def produto_mais_caro(dados, categoria: str) -> dict:
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    O parâmetro "categoria" é uma string contendo o nome de uma categoria.
    Essa função deverá retornar um dicionário representando o produto mais caro da categoria dada.
    '''
    produto_caro = {"id": "", "preco": "", "categoria": ""}

    #encontrar o primeiro produto da categoria.
    for indice_inicial in range(len(dados)):
        if dados[indice_inicial]["categoria"] == categoria:
            produto_caro = dados[indice_inicial]
            break

    for i in range(len(dados)):
        if dados[i]["categoria"] == categoria and float(dados[i]["preco"]) > float(produto_caro["preco"]):
            produto_caro = dados[i]
            
    if produto_caro != {"id": "", "preco": "", "categoria": ""}:
        return produto_caro

    else: return 'Ops... categoria inválida!'

def produto_mais_barato(dados, categoria: str) -> dict:
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    O parâmetro "categoria" é uma string contendo o nome de uma categoria.
    Essa função deverá retornar um dicionário representando o produto mais caro da categoria dada.
    '''
    produto_barato = {"id": "", "preco": "", "categoria": ""}

    #encontrar o primeiro produto da categoria.
    for indice_inicial in range(len(dados)):
        if dados[indice_inicial]["categoria"] == categoria:
            produto_barato = dados[indice_inicial]
            break

    for i in range(len(dados)):
        if dados[i]["categoria"] == categoria and float(dados[i]["preco"]) < float(produto_barato["preco"]):
            produto_barato = dados[i]

    if produto_barato != {"id": "", "preco": "", "categoria": ""}:
        return produto_barato

    else: return 'Ops... categoria inválida!'

def top_10_caros(dados) -> dict:
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    Essa função deverá retornar uma lista de dicionários representando os 10 produtos mais caros.
    '''
    dados.sort(key = lambda x: float(x["preco"]), reverse = True)
    top_10 = dados[:10]

    return top_10

def top_10_baratos(dados) -> dict:
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    Essa função deverá retornar uma lista de dicionários representando os 10 produtos mais baratos.
    '''
    dados.sort(key = lambda x: float(x["preco"]), reverse = False)
    bottom_10 = dados[:10]

    return bottom_10

def menu(dados):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    Essa função deverá, em loop, realizar as seguintes ações:
    - Exibir as seguintes opções:
        1. Listar categorias
        2. Listar produtos de uma categoria
        3. Produto mais caro por categoria
        4. Produto mais barato por categoria
        5. Top 10 produtos mais caros
        6. Top 10 produtos mais baratos
        0. Sair
    - Ler a opção do usuário.
    - No caso de opção inválida, imprima uma mensagem de erro.
    - No caso das opções 2, 3 ou 4, pedir para o usuário digitar a categoria desejada.
    - Chamar a função adequada para tratar o pedido do usuário e salvar seu retorno.
    - Imprimir o retorno salvo. 
    O loop encerra quando a opção do usuário for 0.
    '''

    opcao = int(input(
'''
Escolha um numero, de acordo com as seguintes opções: 
1. Listar categorias
2. Listar produtos de uma categoria
3. Produto mais caro por categoria
4. Produto mais barato por categoria
5. Top 10 produtos mais caros
6. Top 10 produtos mais baratos
0. Sair 

Digite o número desejado:
'''
        ))
    while opcao != 0:
        if opcao == 1:
            print('Categorias da base de dados:')
            pprint.pprint(listar_categorias(dados))

        elif 2 <= opcao <= 4:        
            categoria = input("Escolha uma categoria: ")            
            if opcao == 2:
                print(f'Produtos da categoria {categoria}:')
                pprint.pprint(listar_por_categoria(dados,categoria))
            elif opcao == 3:
                print(f'Produto mais caro da categoria {categoria}:')
                pprint.pprint(produto_mais_caro(dados, categoria))
            elif opcao == 4:
                print(f'Produto mais barato da categoria {categoria}:')
                pprint.pprint(produto_mais_barato(dados, categoria))
        elif opcao == 5:
            print('top 10 produtos mais caros:')
            pprint.pprint(top_10_caros(dados))
        elif opcao == 6:
            print('top 10 produtos mais baratos:')
            pprint.pprint(top_10_baratos(dados))
        else:
            opcao = print("\nOpção inválida!")
        opcao = int(input(''' 
1. Listar categorias
2. Listar produtos de uma categoria
3. Produto mais caro por categoria
4. Produto mais barato por categoria
5. Top 10 produtos mais caros
6. Top 10 produtos mais baratos
0. Sair 
\nEscolha um novo numero: \n'''
        ))
        
    else:
        exit()

# Programa Principal
d = obter_dados()
menu(d)
