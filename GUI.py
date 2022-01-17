from tkinter import *
import sys
import os 

root = Tk()
root.geometry("1200x600")
root.title("S&P50")
root.configure(bg = "#2D2D32")

title = Label(root, text = "S&P 10", fg = "#D5D5D6", bg = '#2D2D32', font = ("Times New Roman",70, "bold"))
title.pack()


def getCrypto():
    info = Label(root, text = crypto.get())
    info.pack()

crypto = Entry(root, width = 50, borderwidth = 1, bg = '#2D2D32')
crypto.pack()
crypto.insert(0, "Enter Crypto")



getInfo_Button = Button(root, text = "Get Info", padx = 100, pady = 70, font = ("Times New Roman",20, "bold"), command = getCrypto)
getInfo_Button.pack()
getInfo_Button.place(x = 200, y = 180)




def randomCrypto():
    os.system("python main.py")

randomButton = Button(root, text = "Random Crypto", bg = "#7C7C7C", padx = 70, pady = 70, font = ("Times New Roman",20, "bold"), command = randomCrypto)
randomButton.pack()
randomButton.place(x = 700, y = 180)





root.mainloop()