from tkinter import *

import sys
import os 

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure

def main():
    root = Tk()
    gui = startPage(root)
    gui.root.mainloop()
    return None

class startPage:
    def __init__(self, root):
        self.root = root
        self.root.title("S&P50")
        self.root.geometry("1200x700")
        self.root.configure(bg = "#2D2D32")

        #Title
        self.title = Label(self.root, text = "S&P 10", fg = "#D5D5D6", bg = '#2D2D32', font = ("Times New Roman",70, "bold"))
        self.title.pack()

        #Search Box
        self.search_box = Entry(self.root, width = 50, borderwidth = 1, bg = '#2D2D32')
        self.search_box.pack(pady = 10)
        self.search_box.insert(0, "Enter Crypto")

        #showButton
        self.showButton = Button(self.root, text = "Show Cryptos", bg = "#7C7C7C",width = 20, height = 5, font = ("Times New Roman",20, "bold"), command = self.show_list_box)
        self.showButton.pack(side = LEFT, padx = 50)

        #randomButton
        self.randomButton = Button(self.root, text = "Random Crypto", bg = "#7C7C7C",width = 20, height = 5, font = ("Times New Roman",20, "bold"), command = self.randomCrypto)
        self.randomButton.pack(side =  RIGHT, padx = 50)

        #Top10 Cryptos
        global cryptos
        cryptos = ["BTC", "ETH", "DOGE", "SHIB", "BCH", "ETC", "BNB", "USDT", "SOL", "ADA"]

        #Cryptos Listbox
        self.list_box = Listbox(self.root, bg = "#BDBDBD", height = 10, width = 40, font = ("Times New Roman",15, "bold"))
        self.list_box.pack(pady = 50)
        # self.list_box.bind("<<ListboxSelect>>", update_search_box)
    

        
    def randomCrypto(self, event = None):
        os.system("python main.py")


    def show_list_box(self, event = None):
        self.list_box.delete(0, END)
        
        for crypto in cryptos:
            self.list_box.insert(END, crypto)
            

    #Update search box with listbox clicked
    def update_search_box(self, e):
        self.search_box.delete(0, END)
        self.search_box.insert(0, self.list_box.get(ACTIVE))




main()