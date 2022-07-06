from cmath import sqrt
from tkinter import *
import numpy as np
import pandas as pd
import math
        
class Normalization(object):
    def __init__ (self, data):
        self.data = data
        
    def normalizacija(self):
        return (self.data - np.min(self.data)) / (np.max(self.data) - np.min(self.data))

class OduzimanjeSrednjeVrednostiNiza(object):   
    def __init__ (self, data):
        self.data = data
    
    def oduzimanje(self):
        return self.data - (np.sum(self.data) / len(self.data))

class StandardnaDevijacija(object):
    def __init__ (self, data):
        self.data = data

    def stdevijacija(self):
        return math.sqrt(np.sum(np.power(self.data - (self.data - (np.sum(self.data) / len(self.data))), 2)) / (len(self.data) - 1))

if __name__ == "__main__":
    data_input = input("Unesi ime fajla: ")
    data = np.loadtxt(data_input)
    rezultat1 = Normalization(data)
    rezultat2 = OduzimanjeSrednjeVrednostiNiza(data)
    rezultat3 = StandardnaDevijacija(data)
     
    #korisnicki interfejs
    #1.komanda za normalizaciju
    def komanda1():
        value = list(lbl_value1["text"])
        lbl_value1["text"] = f"{rezultat1.normalizacija()}"
        
    #2.komanda za oduzimanje
    def komanda2():
        value = list(lbl_value2["text"])
        lbl_value2["text"] = f"{rezultat2.oduzimanje()}"

    #3.komada za standardnu devijaciju
    def komanda3():
        value = list(lbl_value3["text"])
        lbl_value3["text"] = f"{rezultat3.stdevijacija()}"
    
    #komande za cuvanje rezultata odgovarajuce metode u .xlsx fajl   
    def sacuvaj1():
        izlaz1 = rezultat1.normalizacija()
        df = pd.DataFrame({'Normalizacija': izlaz1})
        df.to_excel('demo2.xlsx', index=False)
    
    def sacuvaj2():
        izlaz2 = rezultat2.oduzimanje()
        df = pd.DataFrame({'Oduzimanje': izlaz2})
        df.to_excel('demo2.xlsx', index=False)
    
    def sacuvaj3():
        izlaz3 = rezultat3.stdevijacija()
        df = pd.DataFrame({'Standardna devijacija': [izlaz3]})
        df.to_excel('demo2.xlsx', index=False)
    
    #resetovanje
    def resetovanje():
        value1 = list(lbl_value1["text"])
        value2 = list(lbl_value2["text"])
        value3 = list(lbl_value3["text"])
        lbl_value1["text"] = []
        lbl_value2["text"] = []
        lbl_value3["text"] = []
    
    #zatvaranje aplikacije   
    def close_app():
        window.destroy()
                            
    window = Tk()
    labela = window.title("Transformacija podataka")
    window.geometry("600x500")

    #lab1
    lab1 = Label(master=window, text="Izaberite željenu metodu", font="Arial")
    lab1.grid(row=0, column=0)
    
    #lab2
    lab2 = Label(master=window, text="Rezultati metoda:", font="Arial")
    lab2.grid(row=0, column=1)
    lab2.place(relx=0.53, rely=0, anchor=N)
    
    #dugme1
    btn_normalizacija = Button(master=window, text="normalizacija", command=komanda1, font="Arial")
    btn_normalizacija.grid(row=1, column=0, sticky="nsew")
    
    #labela1
    lbl_value1 = Label(master=window, font="Arial")
    lbl_value1.grid(row=1, column=1)
    
    #dugme2
    btn_razlika= Button(master=window, text="razlika", command=komanda2, font="Arial")
    btn_razlika.grid(row=2, column=0, sticky="nsew")
    
    #labela2
    lbl_value2 = Label(master=window, font="Arial")
    lbl_value2.grid(row=2, column=1)
    
    #dugme3
    btn_stdevijacija= Button(master=window, text="stdevijacija", command=komanda3, font="Arial")
    btn_stdevijacija.grid(row=3, column=0, sticky="nsew")
    
    #labela3
    lbl_value3 = Label(master=window, font="Arial")
    lbl_value3.grid(row=3, column=1)
    
    upit1 = Label(master=window, text="Izaberite tip unosa rezultata metode u .xlsx fajl:" ,font="Arial")
    upit1.place(relx=0.5, rely=0.32, anchor=N)

    #dugmici za unosenje metoda u excel fajl
    btn_unesi1= Button(master=window, text="Unesi1", width=7, height=1, command=sacuvaj1, font="Arial", fg="white", bg="green")
    btn_unesi1.place(relx=0.25, rely=0.4, anchor=N)
    btn_unesi2= Button(master=window, text="Unesi2", width=7, height=1, command=sacuvaj2, font="Arial", fg="white", bg="green")
    btn_unesi2.place(relx=0.5, rely=0.4, anchor=N)
    btn_unesi3= Button(master=window, text="Unesi3", width=7, height=1, command=sacuvaj3, font="Arial", fg="white", bg="green")
    btn_unesi3.place(relx=0.75, rely=0.4, anchor=N)
    
    upit2 = Label(master=window, text="Da li zelite da resetujete rezultate ili da zatvorite aplikaciju?" ,font="Arial")
    upit2.place(relx=0.5, rely=0.51, anchor=N)
    
    #dugme za resetovanje i zatvaranje aplikacije
    btn_resetuj = Button(master=window, text="Resetuj", width=7, height=1, command=resetovanje, font="Arial", fg="white", bg="blue")
    btn_resetuj.place(relx=0.37, rely=0.6, anchor=N)
    btn_zatvori = Button(master=window, text="Zatvori", width=8, height=1, command=close_app, font="Arial", fg="white", bg="red")
    btn_zatvori.place(relx=0.6, rely=0.6, anchor=N)
    
    window.mainloop()