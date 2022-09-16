import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt

df_full = pd.read_csv('campeonato-brasileiro-full.csv',encoding="ISO-8859-1")


def pontuacao(gols_mandante, gols_visitante):   

    if int(gols_mandante) > int(gols_visitante):
        mandante = 3
        visitante = 0
        return mandante, visitante

    elif int(gols_mandante) < int(gols_visitante):
        mandante = 0
        visitante = 3
        return mandante, visitante

    else:
        mandante = visitante = 1
        return mandante, visitante
df_full[['Pontuacao mandante', 'Pontuacao Visitante']] = pd.Series([np.zeros, np.zeros])
for i in range(len(df_full)):
    df_full[['Pontuacao mandante', 'Pontuacao Visitante']].iloc[i] = pontuacao(df_full['mandante_placar'].values[i], df_full['visitante_placar'].values[i])
