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
