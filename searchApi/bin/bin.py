
"""
import requests
import urllib
from bs4 import BeautifulSoup

query = 'Thomas Jefferson'
query = urllib.quote_plus(query)

r = requests.get('https://www.google.com/search?q=site:wikipedia.com+{}&gbv=1&sei=YwHNVpHLOYiWmQHk3K24Cw'.format(query))
soup = BeautifulSoup(r.text, "html.parser")
#creates soup and opens URL for Google. Begins search with site:wikipedia.com so only wikipedia
#links show up. Uses html parser.

links = []
for item in soup.find_all('h3', attrs={'class' : 'r'}):
    links.append(item.a['href'][7:]) # [7:]
    
    
   """
   
 #  =============================================================
import requests
from bs4 import BeautifulSoup

query = 'Thomas Jefferson'

headers = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
}
q = "thomas edison"

"""
#r = requests.get('https://www.google.com/search?q=site:wikipedia.com thomas edison', headers=headers).text
#r = requests.get('https://www.google.com/search?q=site:wikipedia.com', q, headers=headers).text

r = requests.get('https://www.google.com/search?q= thomas edison', headers=headers).text

r = requests.get('https://www.google.com/search?q=',q, headers=headers).text
"""
r = requests.get('https://www.google.com/search?q='+ str(q) , headers=headers).text

soup = BeautifulSoup(r, "html.parser")
#creates soup and opens URL for Google. Begins search with site:wikipedia.com so only wikipedia
#links show up. Uses html parser.
#print(soup)  
with open('bin.txt', 'w', encoding='utf-8') as f_out:
        f_out.write(soup.prettify())

links = []
for item in soup.find_all('div', class_='egMi0'):
    links.append(item.a['href'][7:]) # [7:]
    print(links)
print(links)    
    
    
