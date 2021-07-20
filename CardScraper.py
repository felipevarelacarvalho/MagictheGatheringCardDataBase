from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup

nav = webdriver.Chrome()

card= input('Insert the name of the desired card\'s name: ')
card_name = card.title()

nav.get('https://gatherer.wizards.com/Pages/Default.aspx')

nav.find_element_by_xpath('//*[@id="ctl00_ctl00_MainContent_Content_SearchControls_CardSearchBoxParent_CardSearchBox"]').send_keys(card_name)
nav.find_element_by_xpath('//*[@id="ctl00_ctl00_MainContent_Content_SearchControls_CardSearchBoxParent_CardSearchBox"]').send_keys(Keys.ENTER)
r = requests.get(nav.current_url).text
soup = BeautifulSoup(r, 'html.parser')

if soup.find_all('div', {'class':'cardContent'}):
    print('Found you card!')

else:
    desired_card = soup.find('img', {'alt': card_name })
    for parent in desired_card.parents:
        if parent.name == 'a':
            card_url = str(parent['href'])
            card_url = card_url.replace('..', '')
    treatred_card_url = 'https://gatherer.wizards.com/Pages' + card_url
    print('Found it among many search results!')
    nav.get(treatred_card_url)