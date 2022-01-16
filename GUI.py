from tkinter import *

root = Tk()
root.geometry("1200x600")
root.title("S&P50")
root.configure(bg = "#383847")

title = Label(root, text = "S&P 50", font = ("Lora",50))
title.pack()

crypto = Entry(root, width = 50, borderwidth = 5, )
crypto.pack()



    
randomButton =  Button(root, text = "Next Crypto", padx = 50, pady = 50)
randomButton.pack()


root.mainloop()