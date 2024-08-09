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
for ısım,fıyat, name, price in zip(gzz, ss,dd,ff):
    print(f"{ısım.text.strip()}={fıyat.text.strip()} ---------- {name.text.strip()}={price.text.strip()}  ")
