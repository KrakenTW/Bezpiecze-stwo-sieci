import itertools
import numpy as np

def GET_LFSR():
   
    tempInput = input("Wprowadz kod LFSR ktory chcesz przeanalizowac: ")
    lfsr = []
    for digit in tempInput:
        lfsr.append(int(digit))  # konwertujemy liczby do przekonwertowania 
                                 # zostają one zwrócone w formie tablicy
    return lfsr

def subSequences(lfsr):
    """
    wczytywanie subsekwencji LFSR z pamięci oraz oczyszczanie pamięci programu.
    zwracana jest lista wszystkich kroków wykorzystanych do stworzenia LFSR
    
    """
    allSequences = []

    for item in itertools.product([0, 1], repeat= len(lfsr)):
        allSequences.append(list(item))                 #finds all possible sequences

    subSequencesLength = []
    while len(allSequences) != 0:                       #there are still sequences to be found
        currentSequence = allSequences[0]
        history = []
        lengthOfSubsequence = 0
        while currentSequence not in history:
            result = 0
            history.append(currentSequence)
            for i in range(0,len(lfsr)):
                result = (result + (currentSequence[i]*lfsr[i])) % 2

            newSequence = currentSequence[1:]
            newSequence.append(result)
            currentSequence = newSequence
            lengthOfSubsequence+= 1

        print(history, "length: %d"  % (lengthOfSubsequence))
        subSequencesLength.append(lengthOfSubsequence)
        for i in range(0, len(history)):
            allSequences.remove(history[i])
    print("Lenghts of subsequences: %s " %(subSequencesLength))

def draw(lfsr):
    """
    Draws a given LFSR using tikz and prints tikz commands to console.
    Parameters
    ----------
    lfsr : list
        The LFSR of which all subsequnces are to be found.
    """
    licznik = 0
    listaXOR = []
    listaBox = []
    ostatniBox = 0
    print(r"\begin{tikzpicture}")
    for i in range(0,len(lfsr)):
        print(r"\node[draw,align=left,minimum size=1cm] (%s) at (%s ,0) {$S_{i+%s}$};" % (i, 2*i ,i))       #draws boxes of S_i
        if i == len(lfsr)-1:
            ostatniBox = i
            print(r"\coordinate (end) at ($ (%s) + (2, 0)$);" % (i))        #coordinate of very last box
        listaBox.append('%s' %(i))                               #keeps track of the boxes
        if lfsr[i] == 1:    #if the box is 'enabled'
            if i!= 0:       #and it is not the very first box
                licznik += 1
                listaXOR.append('xor%s' %(i))
                print(r"\node[draw,align=left,minimum size=0.5cm, shape = circle] (xor%s) at (%s, 2) {$+$};" % (i, 2 * i))      #prints the xor symbols above each S_i needed
                print(r"\draw[<-, line width = 0.5mm] (xor%s) -- (%s);" % (i, i))   #prints lines connecting xors and nodes
                if licznik == 1:
                    print(r"\draw[->, line width = 0.5mm] (0, 2) -- (xor%s);" % (i)) #if the licznik=1, connect S_{i} with the first xor
            else:
                print(r"\draw[line width = 0.5mm] (0, 2) -- (%s);" % (i))
    for i in listaXOR:
        if i != listaXOR[len(listaXOR)-1]:
                print(r"\draw[->, line width = 0.5mm] (%s) -- (%s);" % (i, listaXOR[listaXOR.index(i)+1]))
        else:
                print(r"\coordinate (end1) at ($ (%s) + (2, 0)$);" % (i))
                print(r"\draw[line width = 0.5mm] (end1)  -- (%s);" % (i))
                print(r"\draw[line width = 0.5mm] (end)  -- (end1);")
                print(r"\draw[->, line width = 0.5mm] (end)  -- (%s);" %(ostatniBox))

    print(r"\draw[<-, line width = 0.5mm] (-1.5,0) -- (0);")
    for i in range(0, len(lfsr)):
        if i != len(lfsr)-1:
            print(r"\draw[<-, line width = 0.5mm] (%s) -- (%s);" %(i, i+1))
        if lfsr[i] == 1:
             continue
    print(r"\end{tikzpicture}")

def matrix(lfsr):
    """
    pobieramy długość podanego kodu LFSR w formie tablicy za pomocą metody len
    """
    n = len(lfsr)
    identity = np.identity(n)       #indentyfikacja danych
    matrix = np.roll(identity, (-1,0))      #przesunięcie macierzy ku dołowi
    matrix[n-1,n-1] = 0
    for i in range(0,len(lfsr)):
        matrix[i,n-1] = lfsr[i]             #przesunięcie macierzy do jednej z pobliskich lokalizacji
    return matrix

if __name__ == "__main__":
    lfsr = GET_LFSR()
    print(matrix(lfsr))

    subSequences(lfsr)
    draw(lfsr)