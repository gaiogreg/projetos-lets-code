def gera_combinacoes(dic_musicos, instrumentos, banda=[], combinacoes=[],lista_bool = []):
    
    instrumento = instrumentos[0]
    musico_por_instrumento = dic_musicos[instrumento]  
    if type(musico_por_instrumento) == str:
        musico_por_instrumento = [musico_por_instrumento]
    
    for musico in musico_por_instrumento:
     
        booleano_musico = evitar_musicos_duplicados(banda, musico, instrumento)  
        lista_bool.append(booleano_musico) 

        
        booleano_banda = evitar_bandas_duplicadas(combinacoes, banda)
        lista_bool.append(booleano_banda)

        if len(instrumentos) > 1 and booleano_musico:
            combinacoes = gera_combinacoes(dic_musicos,instrumentos[1:], banda, combinacoes, lista_bool)

        elif False not in lista_bool:
            combinacoes.append(banda.copy())
        banda.pop()
        lista_bool.pop()
        lista_bool.pop()

    return combinacoes

def evitar_musicos_duplicados(banda, musico, instrumento):

    banda.append([musico,instrumento])
    for musico_instrumento in banda[:-1]:
            if musico in musico_instrumento:
                return False
    return True

def evitar_bandas_duplicadas(combinacoes, banda):
    lista_bool_banda = []
    for bandas_formadas in combinacoes:
            for musico in banda:
                if musico in bandas_formadas:
                    lista_bool_banda.append(True)
                if len(lista_bool_banda) == 3:
                    return False
            lista_bool_banda = []
    return True

dic_musicos = {'a':['Q','W','R'],'c':['T','Y']}
instrumentos =['a','a','c']

teste = gera_combinacoes(dic_musicos, instrumentos, combinacoes=[])
for banda in teste:
    print(banda)

