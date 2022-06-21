import json

class ErroNome(Exception):
    def __init__(self, mensagem='O nome digitado possui caracteres inválidos!'):
        super().__init__(print(mensagem))

class ErroEmail(Exception):
    def __init__(self, mensagem='Esse e-mail é inválido!'):
        super().__init__(print(mensagem))

class ErroBusqueda(Exception):
    def __init__(self, mensagem='Essa opção é inválida'):
        super().__init__(print(mensagem))

def validar_nome(nome: str):
    nome = nome.lower()
    str_letras = 'qwertyuioplkjhgfdsazxcvbnm '

    for caracter in nome:
        if caracter not in str_letras:
            raise ErroNome

def validar_email(email: str):
    str_chrs = '@qwertyuioplkjhgfdsazxcvbnm0123456789_.'
    for elemento in email:
        if elemento not in str_chrs:
            raise ErroEmail

    if '@' in email:
        for indice in range(len(email)):
            if email[indice] == '@' and email[indice-1] not in str_chrs and email[indice+1] not in str_chrs:
                raise ErroEmail
    else:
        raise ErroEmail

def generos_musicais() -> list:
    pergunta = int(input('Digite o número de gêneros tocados? '))
    return [input(f'Digite o {i+1}o gênero musical: ').title() for i in range(pergunta)]

def instrumentos_tocados() ->  list:
    pergunta = int(input('Digite o número de instrumentos tocados? '))
    return [input(f'Digite o {i+1}o instrumento: ').title() for i in range(pergunta)]

def dados_musicos(ponto_de_partida: int) -> dict or tuple or list:
 
    if 1 <= ponto_de_partida <= 2: #para adicionar musico ou modificá-lo
        email = input('Digite o e-mail: ')
        nome = input('Digite o nome completo: ').title()            
        generos = generos_musicais()
        instrumentos = instrumentos_tocados()
        validar_nome(nome)
        validar_email(email)
        return {email: [nome, generos, instrumentos]}
    
    elif ponto_de_partida == 3: #para o caso de buscar musico
        email = input('Digite o e-mail: ')
        nome = input('Digite o nome completo: ').title()
        genero = input('Digite o gênero que busca: ').title()
        instrumento = input('Digite o instrumento que busca: ').title()
        return [email, nome, genero, instrumento]

    elif ponto_de_partida == 4: #para o caso de montar a banda
        genero = input('Escolha um gênero para sua banda: ').title()
        num_instrumentos = int(input('Quantos instrumentos irão tocar? '))
        instrumento = [input(f'digite o {idx + 1}o instrumento: ').title() for idx in range(num_instrumentos)]
        return (genero, instrumento)

    elif ponto_de_partida == 5: #para sair do programa
        pass

    else:
        raise ErroBusqueda
            
def anexa_musico(dicionario_musicos: dict, dados: dict, chave: str):

    if chave not in dicionario_musicos:
        dicionario_musicos.update(dados)
        dicionario_musicos = json.dumps(dicionario_musicos)

        with open('lista_musicos.json', 'w') as database:
            database.write(dicionario_musicos)
    else:
        print('Usuário já existente!')

def modificar_perfil(dicionario_musicos: dict, dados: dict, chave: str):

    if chave in dicionario_musicos:
        dicionario_musicos.update(dados)

        with open('lista_musicos.json', 'w') as database:
            dicionario_musicos = json.dumps(dicionario_musicos)
            database.write(dicionario_musicos)
            
    else: print('Usuário não encontrado')

def buscar_musico(dicionario_musicos: dict, dados: list, exata_ou_geral):
    
    if exata_ou_geral.lower() == 'exata':

        lista_musicos = []
        contador1 = 0
        
        for dado in dados: # contar número de dados inputados
            if dado != "":
                contador1 += 1

        for musico in dicionario_musicos.items():
            contador2 = 0

            for dado in dados:
                for idx in range(len(musico[1])):
                    if dados[0] == musico[0]:
                        contador2 += 1
                        break

                    elif dado in musico[1][idx] and musico not in lista_musicos and dado != '':
                        contador2 += 1 #contando número de dados que batem com os inputados pelo usuário
                        
                if contador1 == contador2:
                    lista_musicos.append(musico)
                    break
        return lista_musicos
                
    elif exata_ou_geral.lower() == 'geral': 

        lista_musicos = []
        for musico in dicionario_musicos.items():
            for dado in dados:
                for idx in range(len(musico[1])): #musico[1] == ['nome',['generos'],['instrumentos']]

                    if dado in musico[1][idx] and musico not in lista_musicos and dado != '':
                        lista_musicos.append(musico)

                    if dados[0] in dicionario_musicos.keys() and musico not in lista_musicos: #este cuida de verificar se o email consta na base de dados
                        lista_musicos.append((dados[0], dicionario_musicos[dados[0]]))
        
        return lista_musicos
    
    else:
        raise ErroBusqueda

def montar_banda(dicionario_musicos, genero: str, instrumentos) -> dict:
    
    lista_musicos = [(valores[0],instrumento) for instrumento in instrumentos for valores in dicionario_musicos.items() if 
    genero in valores[1][1] and instrumento in valores[1][2]]

    #valores[0] == email
    #valores[1][1] == generos
    #valores[1][2] == instrumentos

    dict_bandas = {}

    for item in lista_musicos:

        instrumento = item[1]
        email = item[0]
        
        if instrumento not in dict_bandas.keys():
            dict_bandas[instrumento] = email

        elif type(dict_bandas[instrumento]) == str:
            lista_emails = [dict_bandas[instrumento]]
            lista_emails.append(email)
            dict_bandas[instrumento] = lista_emails
            
        else:
            lista_emails.append(email)
            dict_bandas[instrumento] = lista_emails

    return gera_combinacoes(dict_bandas, instrumentos)    

def gera_combinacoes(dic_musicos, instrumentos, banda=[], combinacoes=[]):
    
    dic_musicos_copia = dic_musicos.copy()
    instrumento = instrumentos[0]
    musico_por_instrumento = dic_musicos.pop(instrumentos[0])   
    if type(musico_por_instrumento) == str:
        musico_por_instrumento = [musico_por_instrumento]
    instrumentos.remove(instrumentos[0])
    i = 0

    while i in range(len(musico_por_instrumento)):
        if [musico_por_instrumento[i], instrumento] in banda:
            continue        
        i, booleano = evitar_duplicados(banda, musico_por_instrumento, i, instrumento)        
        if instrumentos:
            combinacoes = gera_combinacoes(dic_musicos,instrumentos, banda, combinacoes)
        elif booleano:
            combinacoes.append(banda.copy())
        banda.pop()
        i += 1

    dic_musicos.update({instrumento: musico_por_instrumento})
    instrumentos.append(list(dic_musicos_copia.keys())[0])

    return combinacoes

def evitar_duplicados(banda, musico_por_instrumento, contador, instrumento):

    banda.append([musico_por_instrumento[contador],instrumento])
    for musico_instrumento in banda[:-1]:
            if musico_por_instrumento[contador] in musico_instrumento and len(banda) > 1:
                banda.pop() #removendo duplicados
                try:
                    banda.append([musico_por_instrumento[contador+1],instrumento]) #appending o seguinte termo
                    contador += 1
                except:
                    banda.append([musico_por_instrumento[contador],instrumento])
                    return contador, False

    return contador, True

def menu():
    '''
    1. Criar perfil
    2. Modificar perfil
    3. Buscar Musico
    4. Montar banda
    5. Sair
    '''
    try:
        with open('lista_musicos.json', 'r') as database:    
            dicionario_musicos = json.loads(database.read())    
    except:
        database = open('lista_musicos.json', 'w')
        database.close()

    try:
        ponto_de_partida = int(input('''
O que deseja fazer? (Digite o número correspondente)
1. Criar perfil
2. Modificar perfil
3. Buscar Musico
4. Montar banda
5. Sair
        '''))

        dicionario_entradas = {
        1: anexa_musico,
        2: modificar_perfil,
        3: buscar_musico,
        4: montar_banda
        }

        dados = dados_musicos(ponto_de_partida)
        if 1 <= ponto_de_partida <= 2:
            dicionario_entradas[ponto_de_partida](dicionario_musicos, dados, *dados)
        
        elif ponto_de_partida == 3:
            exata_ou_geral = input('Deseja fazer uma busqueda exata ou geral? ')
            print(dicionario_entradas[ponto_de_partida](dicionario_musicos, dados, exata_ou_geral))

        elif ponto_de_partida == 4:
            bandas = dicionario_entradas[ponto_de_partida](dicionario_musicos, dados[0],dados[1])
            for banda in bandas:
                print('')
                for musico in banda:
                    print(f'{musico[1]}: {musico[0]}')

        elif ponto_de_partida == 5:
            pass
        else:
            raise ErroBusqueda

        continuar = ''
        if ponto_de_partida != 5: #Analisar se iremos continuar rodando o programa.
            continuar = input('\nDeseja continuar? S/N\n').lower()

        if continuar == 's':
            menu()

        elif continuar == 'n' or ponto_de_partida == 5:
            pass
        else:
            raise ErroBusqueda

    except ErroBusqueda:
        ErroBusqueda
        menu()

    except ErroEmail:
        ErroEmail
        menu()
    
    except ErroNome:
        ErroNome
        menu()
    
    except:
        print('Algo de errado aconteceu! Tente novamente...')
        menu()
            
menu()