import yfinance as yf





hh=input("hisse yaz")
try:
   

   aaple=yf.Ticker(hh)
   
   hisse=aaple.history(period="1d")
   if not hisse.empty:
      
      price=hisse['Close'].iloc[-1]
      print(f"{hh} tekrar deneyin: {price:.2f} USD " )
   else:
      
         print("yeniden deneyin")   


except Exception as e:
    print(f"hisse: {str (e)}")

