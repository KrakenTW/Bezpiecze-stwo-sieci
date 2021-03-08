import sys
import tkinter
import base64
from tkinter import *


root = Tk()
root.geometry('800x600')

def button_command():
    text = entry1.get()
    print(text)
    input = entry1.get()
    return input

def cryptography(input, key):
    encoded_chars = []
    for i in len(input):
        key_c = key[i % len(key)]
        encoded_c = chr(ord(input[i]) + ord(key_c) % 256)
        encoded_chars.append(encoded_c)
    encoded_string = "".join(encoded_chars)
    return base64.urlsafe_b64encode(encoded_string)

entry1 = Entry(root, width = 30)
entry1.pack()
Button(root, text="Tekst", command=button_command).pack()
key = open(r"C:\Users\kraken\Desktop\krytpo\Bezpiecze-stwo-sieci\kod.txt")
print(key.read())
cryptography(input, key)


root.mainloop()

