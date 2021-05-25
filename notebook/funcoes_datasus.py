import pandas as pd
from datetime import date
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import ticker

def tranforma_date(data):
    '''
    Função que recebe as colunas no formato Ano/Mês e tranforma retorna um objeto tipo data
    obs:retorna com a data no primeiro dia do mês correspondente
    '''
    dict_mes = {'Jan':'1', 'Fev':'2', 'Mar':'3', 'Abr':'4', 
                'Mai':'5', 'Jun':'6', 'Jul':'7', 'Ago':'8',
               'Set':'9', 'Out':'10', 'Nov':'11', 'Dez':'12'}
    data = [dt.replace(dt[-3:],str(dict_mes[dt[-3:]])) for dt in data]
    data = pd.to_datetime(data, format='%Y/%m')
    return data

def limpa_dados(dados, nome):
    '''
    Função que recebe um conjunto de dados do datasus e faz diversas manipulações:
        
        renomeia a coluna Unidade da Federação para UF para simplificar
        cria uma coluna para cada região
        elimina os números antes do nome dos estados
        elimina a coluna total
        transforma as colunas relacionadas a data em uma coluna apenas(coluna data)
        transforma a coluna data para o tipo date do python
        restringe a data entre fevereiro de 2008 e dezembro de 2019
    '''
    #Renomeando a coluna Unidade da Federação para simplificar a manipulação 
    dados = dados.rename(columns={'Unidade da Federação':'UF'})

    #Criando uma coluna com a região e eliminado os n;umeros da coluna UF
    dict_regiao = {'1':'Norte', '2':'Nordeste', '3':'Sudeste', '4':'Sul','5':'Centro-Oeste'}
    dados['regiao'] = [dict_regiao[uf[0]] for uf in dados['UF']]
    dados['UF'] = [uf[3:] for uf in dados['UF']]
    
    #Tirando a coluna Total 
    dados = dados.drop('Total', axis=1)
    
    #Eliminando dados antes de Fev/2008
    dados = dados.drop(columns=dados.drop(columns=['UF', 'regiao']).loc[:, :'2008/Jan'])

    #Transformando as colunas em uma coluna data
    dados = pd.melt(dados, id_vars=['UF', 'regiao'],var_name='data', value_name=nome)
    
    #Transformando as colunas em tipo data
    dados['data'] = tranforma_date(dados['data'])
    
    #Eliminado dados antes de Fev de 2008 e depois de Dez de 2019
    dez_2019 = date.fromisoformat('2019-12-01')
    rows_drop = dados[dados['data'].dt.date>dez_2019]
        
    #Tirando a coluna Total 
    dados = dados.drop(rows_drop.index)

    return dados

def plot_grafico_linha(dados, y, hue='UF', title=None, ylabel=None, xlabel='Ano/Mês', legend_title=None, formatter=ticker.StrMethodFormatter("{x:,.2f}")):
    '''
    Função que recebe o dataframe e plota um gráfico de linha de cada Unidade Federativa com o eixo x com a data e eixo y os valores numéricos 
    '''
    #Mudando o estilo de fundo
    sns.set_style('darkgrid')
    
    #Criando uma palheta de cores
    sns.set_palette(sns.color_palette("gist_rainbow", len(dados[hue].unique())))
    
    #Criando figura e eixos
    fig, ax = plt.subplots(figsize=(16,8)) 

    #Criando o gráfico 
    sns.lineplot(x='data', y=y, hue=hue, data=dados, ax=ax)

    #Plotando as legendas e mudando o tamanho das fontes
    plt.title(title, fontsize=20)
    plt.xlabel(xlabel, fontsize=15)
    plt.ylabel(ylabel, fontsize=15)
    plt.xticks(pd.date_range(start=dados['data'].unique()[5], end =dados['data'].unique()[-1], freq='6M'),dados.groupby('data').size().index[5::6].strftime('%b/%Y'),fontsize=12, rotation=90)
    plt.yticks(fontsize=12)
    handles, labels = ax.get_legend_handles_labels()
    ax.legend(handles=handles[1:], labels=labels[1:], title=legend_title, bbox_to_anchor=(1, 1), fontsize=12, title_fontsize=15)
    ax.yaxis.set_major_formatter(formatter)
    
    #Mostrando o gráfico
    plt.show()
    