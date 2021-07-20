"""
    File name: interpolationGPS.py
    Author: Felipe Varela Carvalho
    Date created: 5/24/2021
    Date last modified: 6/25/2021
    Python Version: 3.9.5
    Description: Script to interpolate data from file
"""
import requests
from bs4 import BeautifulSoup



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
for div in soup.find_all('div', {'class':'cardtextbox'}):
    print(div.text)