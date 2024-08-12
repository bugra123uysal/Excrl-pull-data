import requests
from bs4 import BeautifulSoup

""" tr borsası """
urlm = " https://www.getmidas.com/canli-borsa/"

    
r = requests.get(urlm)
g = r.content
ff = BeautifulSoup(g, "html.parser")
""" hisse fiyatları """

ss = ff.find_all("td", class_="val")
 

""" hisse ismi çekme """
gzz=ff.find_all("a",class_="title stock-code" )
   
for ısım,fıyat in zip(gzz, ss):
    print(f"{ısım.text.strip()}={fıyat.text.strip()}   ")

""" abd borsası """

tblurl="https://tr.tradingview.com/markets/stocks-usa/market-movers-all-stocks/"
aa=requests.get(tblurl)
bb=aa.content
cc=BeautifulSoup(bb,"html.parser")
""" isim """
dd=cc.find_all('sup', class_="apply-common-tooltip tickerDescription-GrtoTeat")
""" fiyat """
ff=cc.find_all("td", class_="cell-RLhfr_y4 right-RLhfr_y4")
""" sonuç cıkdılar """
for  name, price in zip(dd,ff):
    print(f" {name.text.strip()}={price.text.strip()}  ")


""" kripyo  """
krpturl="https://tr.tradingview.com/markets/cryptocurrencies/prices-all/"
bır=requests.get(krpturl)
ıkı=bır.content
uc=BeautifulSoup(ıkı,"html.parser")

""" isim """
dort=uc.find_all("a", class_="apply-common-tooltip tickerNameBox-GrtoTeat tickerName-GrtoTeat" )
""" fiyat """
bes=uc.find_all("td", class_="cell-RLhfr_y4 right-RLhfr_y4")

for krptisim, krptpricee in zip(dort, bes):
    print(f"{krptisim.text.strip()}= {krptpricee.text.strip()}")