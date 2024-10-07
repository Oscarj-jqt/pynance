#bs4 pour l'analyse et navigation dans HTML ou XML pour extraire les données
import bs4 as bs 
#sauvegarder la liste des tickers dans un fichier
import pickle 
#Requêtes HTTP pour chercher la page wiki
import requests

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

save_sp500_tickers()