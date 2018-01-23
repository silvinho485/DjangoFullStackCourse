import random

import requests
from bs4 import BeautifulSoup


URL = 'https://www.rhymit.com/pt/palavras-terminadas-em-ista'

response = requests.get(URL)

soup = BeautifulSoup(response.text, 'html.parser')
words = soup.find_all('div', {'class': 'w'})
word = random.choice(words)

print(word.text)


# beautifulsoup4==4.6.0
# requests==2.18.4
