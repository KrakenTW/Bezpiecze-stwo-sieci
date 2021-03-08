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
    return list_of_letters

def cryptography(list_of_letters, key):
    klucz = key
    for i in len(list_of_letters):
        print(list_of_letters[i])
    
    
        

entry1 = Entry(root, width = 30)
entry1.pack()
Button(root, text="Tekst", command=button_command).pack()
key = open(r"C:\Users\kraken\Desktop\krytpo\Bezpiecze-stwo-sieci\kod.txt")
print(key.read())
list_of_letters = list(str(entry1))
print(list_of_letters)
cryptography(list_of_letters,key)
print(len(list_of_letters))


root.mainloop()

