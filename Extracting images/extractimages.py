import requests
from bs4 import BeautifulSoup
r=requests.get('https://www.geeksforgeeks.org/python-programming-language/?ref=shm')

soup=BeautifulSoup(r.content,'html.parser')
images_list=[]
images =soup.select('img')
for image in images:
    src=image.get('src')
    alt=image.get('alt')
    images_list.append({'src':src,'alt':alt})

for im in images_list:
    print(im)
