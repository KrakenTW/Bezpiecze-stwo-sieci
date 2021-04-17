def railfence_encrypt(word, n):
    if n <= 1:
        return word

    ascending = False
    encrypted = n * [""]
    counter = 0

    for letter in word:
        encrypted[counter] += letter
        if ascending:
            counter -= 1
            if counter == 0:
                ascending = False
        else:
            counter += 1
            if counter == n - 1:
                ascending = True

    return "".join(encrypted)


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
