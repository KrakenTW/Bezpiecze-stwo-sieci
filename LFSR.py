import itertools
import binascii
import numpy as np
from os import X_OK, path
from functools import reduce
from operator import xor

class GLFSR:
    def __init__(self, polynomial, seed):
        self.polynomial = polynomial | 1
        self.seed = seed
        self.data = seed
        self.mask = 1

        temp_mask = polynomial
        while temp_mask != 0:
            if temp_mask & self.mask != 0:
                temp_mask = temp_mask ^ self.mask
            if temp_mask == 0: break
            self.mask = self.mask << 1

    def states(self, repeat=False):
        while True:
            self.data = self.data << 1
            if self.data & self.mask != 0:
                self.data = self.data ^ self.polynomial
                yield 1
            else:
                yield 0
            if repeat == False and self.data == self.seed:
                return

def lfsr(seed, taps,dl):
    repeat = 0
    sr, xor = seed, 0
    key = []
    while 1:
        
        if(int(sr[0]) == 0 and int(sr[3]) == 0):
            key.append("0")
            
        if(int(sr[0]) == 1 and int(sr[3]) == 1):
            key.append("1")
            
        if(int(sr[0]) == 1 and int(sr[3]) == 0):
            key.append("0")
            
        if(int(sr[0]) == 0 and int(sr[3]) == 1):
            key.append("1")

        repeat = repeat + 1

        for t in taps:
            xor += int(sr[t-1])
        if xor%2 == 0.0:
            xor = 0
        else:
            xor = 1
        sr, xor = str(xor) + sr[:-1], 0
        
            
        if repeat == dl:
            return key

def listToString(s): 
    '''
    zamiana listy na string wymagany do dzialania lfsr
    '''
    str1 = "" 
    
    for ele in s: 
        str1 += ele  
    
    return str1 

def tekst_to_bytes(tekst):
    
    test_str = tekst 
    
    res = ''.join(format(i, '08b') for i in bytearray(test_str, encoding ='utf-8'))
    
    print("tekst:  " + str(res))
    return str(res)   

def Cipher(BinTekst, key, dlBin):
    a = BinTekst
    b = key
    max_len = max(len(a), len(b))
    a = a.zfill(max_len)
    b = b.zfill(max_len)
    
    # Initialize the result
    result = ''
    
    # Initialize the carry
    carry = 0
    
    # Traverse the string
    for i in range(max_len - 1, -1, -1):
        r = carry
        r += 1 if a[i] == '1' else 0
        r += 1 if b[i] == '1' else 0
        result = ('1' if r % 2 == 1 else '0') + result
    
        # Compute the carry.
        carry = 0 if r < 2 else 1
    
    if carry != 0:
        result = '1' + result
    
    return result

def CipherDec(s1, s2):
    return bin(int(s1, 2) - int(s2, 2))[2:]
 


#Wprowadzanie danych
tempInput = input("Wprowadz kod LFSR ktory chcesz przeanalizowac: ")
Tekst = input("Wprowadz tekst do zaszyfrowania:  ")
#Zamiana tekstu na bity
BinTekst = tekst_to_bytes(Tekst)
#pobranie potrzebnej długości klucza
dlBin = len(BinTekst)
#stworzenie klucza oraz utworzenie z niego stringa
key = lfsr(seed= tempInput, taps = (1,4),dl= dlBin)      #example
key = listToString(key)
#Zaszyfrowany tekst za pomocą stworzonego klucza
Zaszyfrowane = Cipher(BinTekst, key, dlBin)
str_data =' '
Zaszyfrowane = CipherDec(Zaszyfrowane,key) #odszyfrowanie
while len(Zaszyfrowane) < len(BinTekst):
    Zaszyfrowane = "0" + Zaszyfrowane
binary_int = str(Zaszyfrowane)
str_data= [Zaszyfrowane[i:i+8] for i in range(0, len(Zaszyfrowane), 8)]
print(Zaszyfrowane)
# printing the result
print("Odszyfrowane:", str_data)



        


