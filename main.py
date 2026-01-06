import requests
from bs4 import BeautifulSoup
target_url = "https://karabuknethaber.com/"
response = requests.get(target_url)
soup = BeautifulSoup(response.text, "html.parser")
link_liste=[]

for link in soup.find_all("a"):
    bulunan_link=link.get("href")
    if bulunan_link not in link_liste:
        link_liste.append(bulunan_link)
        print(bulunan_link)
