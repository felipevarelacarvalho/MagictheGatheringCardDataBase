"""
    File name: CraperRequest.py
    Author: Dumith Bou-Habib
    Date created: 07/20/2021
    Date last modified: 07/21/2021
    Python Version: 3.9.5
    Description: Script to scrape mtg cards info
"""
import requests
from bs4 import BeautifulSoup

lables = ['Community Rating','Card Name', 'Mana Cost', 'Converted Mana Cost', 'Types', 'Card Text', 'Flavor Text', 'P/T', 'Expansion', 'Rarity', 'Something', 'Artist']
values = []

card_name = input('$ Name your card: ')
card_name = card_name.title()
card_name_url = card_name.replace(' ', ']+[')
card_name_url = '[' + card_name_url + ']'


r = requests.get('https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+' + card_name_url).text


soup = BeautifulSoup(r, 'html.parser')

try:
    if soup.find_all('div', {'class':'cardContent'}):
        print('Found your card!')

    else:
        desired_card = soup.find('img', {'alt': card_name })
        
        for parent in desired_card.parents:
            if parent.name == 'a':
                card_url = str(parent['href'])
                card_url = card_url.replace('..', '')
                
        treatred_card_url = 'https://gatherer.wizards.com/Pages' + card_url
        print('Found it among many search results!')
        r = requests.get(treatred_card_url).text
except AttributeError:
    print('\n-------\nName written incorrectly or this card doesn\'t exist yet!\n-------\n')


soup = BeautifulSoup(r, 'html.parser')
for div in soup.find_all('div', {'class':'value'}):
    dados_da_carta = div.text
    dados_da_carta = dados_da_carta.strip()
    values.append(dados_da_carta)

for i in values:
    print(i)
