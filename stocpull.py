
import requests
from bs4 import BeautifulSoup
urlm = " https://www.getmidas.com/canli-borsa/"
    
r = requests.get(urlm)
g = r.content
ff = BeautifulSoup(g, "html.parser")
""" hisse fiyatları """

ss = ff.find_all("td", class_="val")
 

""" hisse ismi çekme """
gzz=ff.find_all("a",class_="title stock-code" )
   
for ısım,fıyat in zip(gzz, ss):
    print(f"{ısım.text.strip()}={fıyat.text.strip()} ")