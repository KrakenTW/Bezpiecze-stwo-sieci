import tkinter
import argparse

root = tkinter.Tk()
root.geometry("1024x768")

mainMenu = tkinter.Menu()

root.config(menu=mainMenu)

fileMenu = tkinter.Menu(mainMenu)

mainMenu.add_cascade(label='Szyfr', menu = fileMenu)
def button_RailFence():
    
    RailFence = entry1.get()
    
    list_of_letters = str(RailFence)
    
    print(list_of_letters)
    
    word = railfence_encrypt(word = list_of_letters, n = 3)
    print("zaszyfrowane " + word)
    decrypt = decrypt_rail_fence(word, 3)
    print("rozszyfrowane  " + decrypt)
    return RailFence
#cipher of railfence 
def railfence_encrypt(word, n):
    if n <= 1:
        return word

    ascending = False
    encrypted = n * ['']
    counter = 0

    for letter in word:
        encrypted[counter] += letter
        if ascending:
            counter -= 1
            if counter == 0:
                ascending = False
        else:
            counter += 1
            if counter == n-1:
                ascending = True
    
    return ''.join(encrypted)

def button_MatrixA():
        
    MatrixA = entry2.get()
    
    list_of_letters = str(MatrixA)
    print(list_of_letters)
    encrypted_message = matrix_encryption(word=list_of_letters, secret_key = "2-1-3")
    print(encrypted_message)
    

def button_MatrixB():
        
    MatrixB = entry3.get()

    list_of_letters = list(str(MatrixB))
    print(list_of_letters)
    secret_key = "3-1-4-2"
    return MatrixB

entry1 = tkinter.Entry(root, width=30)
entry1.pack()
tkinter.Button(root, text="RailFence", command=button_RailFence).pack()


entry2  = tkinter.Entry(root , width=30)
entry2.pack()
tkinter.Button(root, text="MatrixA", command=button_MatrixA).pack()

entry3  = tkinter.Entry(root , width=30)
entry3.pack()
tkinter.Button(root, text="MatrixA", command=button_MatrixB).pack()




def encrypt_rail_fence(text, key):

    rail = [["\n" for i in range(len(text))] for j in range(key)]

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
            if rail[i][j] != "\n":
                result.append(rail[i][j])
    return "".join(result)


def decrypt_rail_fence(cipher, key):

    rail = [["\n" for i in range(len(cipher))] for j in range(key)]

    dir_down = None
    row, col = 0, 0

    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False

        rail[row][col] = "*"
        col += 1

        if dir_down:
            row += 1
        else:
            row -= 1

    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if (rail[i][j] == "*") and (index < len(cipher)):
                rail[i][j] = cipher[index]
                index += 1

    result = []
    row, col = 0, 0
    for i in range(len(cipher)):

        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False

        if rail[row][col] != "*":
            result.append(rail[row][col])
            col += 1

        if dir_down:
            row += 1
        else:
            row -= 1
    return "".join(result)
def _string_to_matrix(str_in: str):
    """ Creates square matrix from string input """
    nums = list(str_in)
    n = int(len(nums) ** 0.5)
    return list(map(list, zip(*[map(str, nums)] * n)))


def matrix_encryption(word: str, secret_key: str):
    """
    Encrypt/decrypt word using matrix shift
    word : str
    Actual word to encrypt
    key: str
    integeres separeted with `-`. This parameter determine
    shift order.
    """
    secret_key = secret_key.split("-")
    matrix = _string_to_matrix(str(word))
    if len(matrix[0]) != len(secret_key):
        raise ValueError("Klucz musi być tej samej długości co ilość kolumn macierzy.")
    encrypted_word = ""
    for word in matrix:
        for i, j in enumerate(secret_key):
            encrypted_word += word[int(j) - 1]
    encrypted_word = "".join(map(str, encrypted_word))

    return encrypted_word


def _word_to_matrix(word, secret_key):
    """Convert word into matrix with secret_key based length
    Temu chyba bliżej do tego co w zadaniu przynajmniej podpunktowi B
    """
    big_arr = []
    temp_arr = []
    word = list(word)
    while word:
        while len(temp_arr) < len(secret_key):
            try:
                temp_arr.append(word.pop(0))
            except IndexError:
                break
        big_arr.append(temp_arr)
        temp_arr = []
    return big_arr


def matrix_shift(word: str, secret_key: str):
    secret_key = secret_key.split("-")
    matrix = _word_to_matrix(word, secret_key)
    if len(matrix) != len(secret_key):
        raise ValueError("Klucz musi być tej samej długości co ilość kolumn macierzy.")
    encrypted_word = ""
    for w in matrix:
        for i, j in enumerate(secret_key):
            try:
                encrypted_word += w[int(j) - 1]
            # Niektóre komórki w ostatni wierszu mogą być puste i przy niekorzystnym ułożeniu klucza
            # może pojawić się odwołanie do nieistniejącej komórki
            except IndexError:
                continue
    encrypted_word = "".join(map(str, encrypted_word))

    return encrypted_word

#def Railword(word: str, secret_key: str):
 #   word = matrix_shift(word="CRYPTOGRAPHYOSA", secret_key='3-1-4-2')
  #  print(word)
   # return None


if __name__ == "__main__":
    encrypted_message = matrix_encryption(word="CRYPTOGRAPHYOSA", secret_key = "3-1-2")
    fileMenu.add_command(label = 'Rail Fence')
    fileMenu.add_separator()
    fileMenu.add_command(label = 'Przestawienie macierzowe A')
    fileMenu.add_separator()
    fileMenu.add_command(label = 'Przestawienie macierzowe B')





root.mainloop()
