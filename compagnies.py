#bs4 pour l'analyse et navigation dans HTML ou XML pour extraire les données
import bs4 as bs
import datetime as dt
import os
import pandas as pd
import pandas_datareader.data as web
import yfinance as yf
#bibliothèque pour les tableaux (arange,array...)
import numpy as np
#sauvegarder la liste des tickers dans un fichier
import pickle 
#Requêtes HTTP pour chercher la page wiki
import requests

from matplotlib import style
import matplotlib.pyplot as plt
style.use('ggplot')

def save_sp500_tickers():
    #fetch la page wiki
    resp = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    #analyse le contenu avec le parser lxml (+ rapide et efficace que HTML)
    soup = bs.BeautifulSoup(resp.text,"lxml")
    #Extraction des données
    #Trouve le tableau 
    table = soup.find('table', {'class':'wikitable sortable'})
    tickers = []
    #On parcours chaque ligne et récupère le premier élément
    for row in table.findAll('tr')[1:] :
        cells = row.findAll('td')
        if len(cells) > 0:  # Vérifier que la ligne contient des cellules
            ticker = cells[0].text.strip()  # Nettoyer les espaces inutiles
            tickers.append(ticker)
    #Sauvegarde dans un fichier pickle
    with open("sp500tickers.pickle","wb") as f:
        pickle.dump(tickers, f)

    print(tickers)

    return tickers

# save_sp500_tickers()

def get_data_form_yahoo(reload_sp500=False) :

    if reload_sp500:
        tickers = save_sp500_tickers()
    else:
        with open("sp500tickers.pickle", "rb") as f:
            tickers = pickle.load(f)

    if not os.path.exists('stock_dfs') :
        os.makedirs('stock_dfs')

    start = dt.datetime(2000,1,1)
    end = dt.datetime(2016,12,31)

    for ticker in tickers :
        print(ticker)
        if not os.path.exists('stock_dfs/{}.csv'.format(ticker)):
            df = yf.download(ticker, start=start, end=end)
            df.to_csv('stock_dfs/{ticker}.csv')
        else:
            print('Il y est déjà {ticker}')

# get_data_form_yahoo()

def compile_data():
    with open("sp500tickers.pickle", "rb") as f:
        tickers = pickle.load(f)

        main_df = pd.DataFrame()

        for count,ticker in enumerate(tickers):
            df = pd.read_csv('stock_dfs/{}.csv'.format(ticker))
            df.set_index('Date', inplace = True)
    
            df.rename(columns = {'Adj Close': ticker}, inplace=True)
            df.drop(['Open','High','Low','Close','Volume'], axis=1, inplace = True)

            if main_df.empty:
                main_df = df
            else:
                main_df = main_df.join(df, how ='outer')

            if count % 10 == 0:
                print(count)

        print(main_df.head())
        main_df.to_csv('sp500_joined_closes.csv')

# compile_data()

def visualize_data():
    #lecture du fichier
    df = pd.read_csv('sp500_joined_closes.csv')
    #Traçage des prix d'Apple
    df['AAPL'].plot()
    # plt.show()
    #Calcul de la matrice de corrélation
    df_corr = df.corr()

    print(df_corr.head())

    data = df_corr.values
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    #Affichage de la heatmap du rouge au vert
    heatmap = ax.pcolor(data, cmap = plt.cm.RdYlGn)
    fig.colorbar(heatmap)
    ax.set_xticks(np.arange(data.shape[0]) + 0.5, minor=False)
    ax.set_yticks(np.arange(data.shape[1]) + 0.5, minor=False)
    ax.invert_yaxis()
    ax.xaxis.tick_top()

    column_lables = df_corr.columns
    row_labels = df_corr.index

    ax.set_xticklabels(column_lables)
    ax.set_yticklabels(row_labels)
    plt.xticks(rotation=90)
    heatmap.set_clim(-1,1)
    plt.tight_layout()
    plt.show()



visualize_data()
