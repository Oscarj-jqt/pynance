# Import de la bibliothèque gérant les dates
import datetime as dt
# gestion de graphiques (analyse de donnée)
import matplotlib.pyplot as plt
#styliser les graphiques
from matplotlib import style
#Pandas  (bibliothèque) pour la manipulation et analyse de donnée
import pandas as pd

# bibliothèque pour graphique financiers
import mplfinance as mpf

# gérer les dates dans les graphiques 
import matplotlib.dates as mdates

# Extrait des données financières externes (Yahoo et Google Finance)
import pandas_datareader.data as web 
# même chose mais solution plus robuste avec API plus fonctionnelle
import yfinance as yf

#style ggplot aux graphiques
style.use('ggplot')
# création date de "début" le 1er janvier 2000
# start = dt.datetime(2000,1,1)
# # date 31 décembre 2016
# end = dt.datetime(2016,12,31)

# Ajuster les options d'affichage pour montrer toutes les colonnes
# pd.set_option('display.max_columns', None)  # Affiche toutes les colonnes
# pd.set_option('display.expand_frame_repr', False)  # Évite le wrapping des lignes

#récupération des données finances pour l'action Tesla depuis Yahoo entre les 2 dates
# df = web.DataReader('TSLA', 'yahoo', start, end)
# Télécharger les données de l'action
# df = yf.download('TSLA', start, end)
#df le DataFrame Pandas et head affiche les premières lignes

# plt.figure(figsize=(12, 6))
# plt.plot(df['Close'], label='Prix de Clôture', color='blue')
# plt.title('Prix de Clôture de Tesla (2000-2016)')
# plt.xlabel('Date')
# plt.ylabel('Prix en USD')
# plt.legend()
# plt.show()
# exportation des données au format csv dans le fichier tsla.csv
# df.to_csv('tsla.csv')
# print(df.head())
df = pd.read_csv('tsla.csv', parse_dates = True, index_col = 0)


# print(df[['Open', 'High']].head()) # Afficher les colonnes Open et High
# df['Adj Close'].plot

#Partie 3

# Calcul de la moyenne mobile sur 100 Jours  (analyse sur le long terme)
df['100ma'] = df['Adj Close'].rolling(window=100, min_periods=0).mean()
# Suppression des valeurs manquantes

df_ohlc = df['Adj Close'].resample('10D').ohlc()
df_volume = df['Volume'].resample('10D').sum()

#Graphique partie 3
# ax1.plot(df.index, df['Adj Close'])
#  ax1.plot(df.index, df['100ma'])
# ax2.bar(df.index, df['Volume'])

#Partie 4


#Conversion des dates pour matplotlib
# df_ohlc['Date'] = pd.to_datetime(df_ohlc['Date'])


# # Réinitialisation de l'index
df_ohlc.reset_index('Date', inplace=True)



# print(type(df_ohlc.index))



# # Création des sous-graphiques 
# ax1 = plt.subplot2grid((6,1), (0,0), rowspan = 5, colspan=1)
# ax2 = plt.subplot2grid((6,1), (5,0), rowspan = 1, colspan=1, sharex=ax1)

# #  Configuration de l'axe des dates
# ax1.xaxis_date()

# #Tracé du graphique en chandeliers
# mpf.plot(df_ohlc, type='candle', ax=ax1)
# # Tracé du volume des transactions
# ax2.fill_between(df_volume.index.map(mdates.date2num), df_volume.values, 0)


df_ohlc['Date'] = df_ohlc['Date'].map(mdates.date2num)
# print(df_ohlc.head())


 