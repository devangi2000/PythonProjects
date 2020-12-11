
import requests
from bs4 import BeautifulSoup

#a=str(input())
#url = 'https://domaineye.com/similar/'+a
url = 'https://www.srmist.edu.in/' 
print(url)
source_code=requests.get(url)
plain_text=source_code.text
soup=BeautifulSoup(plain_text)
for link in soup.findAll('a'):
    href=link.get('href')
    print(href)