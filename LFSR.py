import itertools
import binascii
import numpy as np
from os import X_OK, path


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
    # initializing string 
    test_str = tekst
    
    # printing original string 
    print("The original string is : " + str(test_str))
    
    # using join() + bytearray() + format()
    # Converting String to binary
    res = ''.join(format(i, '08b') for i in bytearray(test_str, encoding ='utf-8'))
    
    # printing result 
    print("tekst:  " + str(res))
    return str(res)   

def Cipher(BinTekst, key, dlBin):
    Ciphered = key
    i = 1
    while i != dlBin:
        if BinTekst[:i] == 0:
            if key[:i] == 0:
                Ciphered[:i] = "0"
            else:
                Ciphered[:i] = "1"
        else:
            if key[:i] == 0:
                Ciphered[:i] = "0"
            else:
                Ciphered[:i] = "1"
        
    print(Ciphered)
    return Ciphered

tempInput = input("Wprowadz kod LFSR ktory chcesz przeanalizowac: ")
Tekst = input("Wprowadz tekst do zaszyfrowania:  ")
BinTekst = tekst_to_bytes(Tekst)
dlBin = len(BinTekst)
key = lfsr(tempInput, (1,4), dlBin)      #example
key = listToString(key)
print("klucz:  " + key)
Zaszyfrowane = Cipher(BinTekst, key, dlBin)

print("ciphe:  " + Zaszyfrowane)

