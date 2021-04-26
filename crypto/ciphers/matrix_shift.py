import numpy as np

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


# Clean this code
class Matrix:
    def __init__(self, key, input):
        self.key_value_list = self.set_values_to_keys_letters(key)
        row_length = self.get_row_length()
        matrix_cells = []
        key_letters_used = 0
        input = list(input)
        while input:
            column = []
            print(key_letters_used)
            key_letter = self.key_value_list[key_letters_used]
            print(f"KEY LETTER {key_letter}")
            remaining_letters_inserted_to_row_counter = key_letter.value
            for row_index in range(0, row_length):
                if remaining_letters_inserted_to_row_counter > 0:
                    print(remaining_letters_inserted_to_row_counter)
                    try:
                        character = input.pop(0)
                        print(f"tu jest {character}")
                    except:
                        character = ""
                        print("zle")
                    remaining_letters_inserted_to_row_counter -= 1
                else:
                    print("tu w ogole jest?")
                    character = "1"
                column.append(character)

            matrix_cells.append(column)
            key_letters_used += 1

        self.matrix_cells = matrix_cells

    def set_values_to_keys_letters(self, key):
        sorted_letters = sorted(key)
        key_value_list = [KeyValue(letter, count + 1) for count, letter in enumerate(sorted_letters)]
        sorted_key_value_list = []
        for letter in key:
            for i, letterObject in enumerate(key_value_list):
                if letterObject == letter:
                    letter_object_index = key_value_list.index(letterObject)
                    let = key_value_list.pop(letter_object_index)
                    sorted_key_value_list.append(let)
                    break
        return sorted_key_value_list

    def get_row_length(self):
        highest = 0
        for letterObject in self.key_value_list:
            if letterObject > highest:
                highest = letterObject.value
        return highest

    def render(self):
        for row in self.matrix_cells:
            for value in row:
                print(value)

    def encrypt(self):
        transponed_matrix = np.transpose(self.matrix_cells)
        for row in transponed_matrix:
            for value in row:
                if not value == "1":
                    print(value)


class KeyValue:
    def __init__(self, character=None, value=None):
        self.character = character
        self.value = value

    def __eq__(self, other):
        return True if self.character == other else False

    def __gt__(self, other):
        return True if self.value > other else False

    def __lt__(self, other):
        return True if self.value < other else False

    def __str__(self):
        return f"Character: {self.character}, Value: {self.value}"
