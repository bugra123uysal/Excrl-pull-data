import yfinance as yf

import tkinter as tk 
from tkinter import ttk


ff=tk.Tk()
ff.geometry=("600x800")

   
while True:
    hh=input("hisse yazı")
    if hh.lower()=="bitti":
        print("bitti")
        break

    else:
        print("girdiler")
        
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
        

ff.mainloop()
