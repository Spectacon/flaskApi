import requests
from bs4 import BeautifulSoup


headers = {
  'User-agent':
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
}
"""
params = {
  "q": "python memes",
  "hl": "en"
}

r = requests.get('https://www.google.com/search', headers=headers, params=params).text

"""

q = "goats+in+trees"

res = requests.get('https://www.google.com/search?q='+ str(q) , headers=headers)

soup = BeautifulSoup(res.text, "html.parser")

with open('binny.txt', 'w', encoding='utf-8') as f_out:
        f_out.write(soup.prettify())
"""
#for result in soup.select('.yuRUbf'):
for result in soup.select('.egMi0'):
  #title = result.select_one('.DKV0Md').text
  title = result.select_one('.l97dzf').text
  url = result.a['href']
  print(f'{title},\n {url}\n')

"""
for result in soup.select('.EASEnb'):
      #title = result.select_one('.DKV0Md').text
  title = result.select_one('.EASEnb').text
  url = result.a['href']
  print(f'{title},\n {url}\n')
