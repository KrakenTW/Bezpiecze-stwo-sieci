import sys
import tkinter
import base64
from tkinter import *


root = Tk()
root.geometry('800x600')

def button_command():
    text = entry1.get()
    list_of_letters = list(str(text))
    print(list_of_letters)
    input = entry1.get()
    cryptography(list_of_letters,key)
    
    

def cryptography(list_of_letters, key):
    klucz = key
    dl = len(list_of_letters)
    
    for i in range(dl):
        kodowanie = 0
        while(kodowanie <= dl):
            print(list_of_letters[kodowanie])
            kodowanie = new_func(kodowanie)

def new_func(kodowanie):
    return kodowanie + 4
    
    
        

entry1 = Entry(root, width = 30)
entry1.pack()
Button(root, text="Tekst", command=button_command).pack()
key = open(r"C:\Users\kraken\Desktop\krytpo\Bezpiecze-stwo-sieci\kod.txt")



root.mainloop()

