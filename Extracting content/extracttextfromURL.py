import requests
from bs4 import BeautifulSoup
r = requests.get("https://www.geeksforgeeks.org/python-programming-language/")
# printing the content of the page with html tags
print(r)
soup = BeautifulSoup(r.content, 'html.parser')
print(soup.prettify())
print("\n")

# printing the title of the page
print(soup.title)

# printing the title of the page without html tags
print(soup.title.name)

# printing the title of the page without html tags
print(soup.title.parent.name)

print('\n')
s = soup.find('div', class_='entry-content')
content = s.find_all('p')

# printing the content of the page with html tags
print(content)

print('\n')
s1 = soup.find('div', id='main')
leftbar = s1.find('ul', class_='leftBarList')
content = leftbar.find_all('li')

# printing the content of the left bar with html tags
print(content)

# printing the content of the page without html tags
print('\n')
lines = s.find_all('p')
for line in lines:
    print(line.text)

# printing the content of the left bar without html tags
letfbarlines = leftbar.find_all('li')
for line in letfbarlines:
    print(line.text)
