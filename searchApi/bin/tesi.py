from bs4 import BeautifulSoup
import requests, lxml

headers = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
}

response = requests.get( 'https://www.google.com/search?q=site:wikipedia.com thomas edison', headers=headers).text

soup = BeautifulSoup(response, 'lxml')

for links in soup.find_all('div', class_='LC20lb MBeuO DKV0Md'):
    link = links.a['href']
    print(link)

# or using select() which uses CSS selectors

for links in soup.select('.yuRUbf a'):
    link = links['href']
    print(link)


# Alternative method using SerpApi

# import os
# from serpapi import GoogleSearch

# params = {
#     "engine": "google",
#     "q": "site:wikipedia.com thomas edison",
#     "api_key": os.getenv("API_KEY"),
# }

# search = GoogleSearch(params)
# results = search.get_dict()

# for result in results["organic_results"]:
#   print(f"Link: {result['link']}")
