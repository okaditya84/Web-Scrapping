import requests
from bs4 import BeautifulSoup
r=requests.get('https://www.geeksforgeeks.org/python-programming-language/?ref=shm')
soup=BeautifulSoup(r.content,'html.parser')
for link in soup.find_all('a'):
    print(link.get('href'))