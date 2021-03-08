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
    return text
    
    

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
    
    
  
def encryptRailFence(text, key): 
  
    rail = [['\n' for i in range(len(text))] 
                  for j in range(key)] 
      
    dir_down = False
    row, col = 0, 0
      
    for i in range(len(text)): 
          
        if (row == 0) or (row == key - 1): 
            dir_down = not dir_down 
          
        rail[row][col] = text[i] 
        col += 1
          
        if dir_down: 
            row += 1
        else: 
            row -= 1
    result = [] 
    for i in range(key): 
        for j in range(len(text)): 
            if rail[i][j] != '\n': 
                result.append(rail[i][j]) 
    return("" . join(result)) 
      
def decryptRailFence(cipher, key): 
  
    
    rail = [['\n' for i in range(len(cipher))]  
                  for j in range(key)] 
     
    dir_down = None
    row, col = 0, 0
       
    for i in range(len(cipher)): 
        if row == 0: 
            dir_down = True
        if row == key - 1: 
            dir_down = False
          
        rail[row][col] = '*'
        col += 1
          
        if dir_down: 
            row += 1
        else: 
            row -= 1
              
    index = 0
    for i in range(key): 
        for j in range(len(cipher)): 
            if ((rail[i][j] == '*') and
               (index < len(cipher))): 
                rail[i][j] = cipher[index] 
                index += 1
          
    result = [] 
    row, col = 0, 0
    for i in range(len(cipher)): 
          
        if row == 0: 
            dir_down = True
        if row == key-1: 
            dir_down = False
              
        if (rail[row][col] != '*'): 
            result.append(rail[row][col]) 
            col += 1
              
        if dir_down: 
            row += 1
        else: 
            row -= 1
    return("".join(result)) 
  
if __name__ == "__main__": 
    print(encryptRailFence("geeek", 2)) 
    print(encryptRailFence("GeeksforGeeks ", 3)) 
    print(encryptRailFence("defend the east wall", 3)) 
      
    print(decryptRailFence("GsGsekfrek eoe", 3)) 
    print(decryptRailFence("atc toctaka ne", 2)) 
    print(decryptRailFence("dnhaweedtees alf tl", 3)) 
  

        

entry1 = Entry(root, width = 30)
entry1.pack()
Button(root, text="Tekst", command=button_command).pack()
text = button_command
length = len(text)
print(text)
print(length)
key = open(r"C:\Users\kraken\Desktop\krytpo\Bezpiecze-stwo-sieci\kod.txt")



root.mainloop()

