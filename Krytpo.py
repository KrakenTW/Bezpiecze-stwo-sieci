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
    print("zaszyfrowane Rail " + word)

    decrypt = decrypt_rail_fence(word, 3)
    print("rozszyfrowane  Rail " + decrypt)
    return RailFence


def button_MatrixA():     
    MatrixA = entry2.get()
    list_of_letters = str(MatrixA)
    print(list_of_letters)

    encrypted_message = matrix_encryption(word=list_of_letters, secret_key = "2-1-3")
    print("zaszyfrowane matrix " + encrypted_message)

    decrypt = matrix_encryption(word=encrypted_message, secret_key = "2-1-3")
    print("rozszyfrowane matrix " + decrypt)
    

    

entry1 = tkinter.Entry(root, width=30)
entry1.pack()
tkinter.Button(root, text="RailFence", command=button_RailFence).pack()


entry2  = tkinter.Entry(root , width=30)
entry2.pack()
tkinter.Button(root, text="MatrixA", command=button_MatrixA).pack()


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





if __name__ == "__main__":
    fileMenu.add_command(label = 'Rail Fence')
    fileMenu.add_separator()
    fileMenu.add_command(label = 'Przestawienie macierzowe A')
    fileMenu.add_separator()
    fileMenu.add_command(label = 'Przestawienie macierzowe B')





root.mainloop()
