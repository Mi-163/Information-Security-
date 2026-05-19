def encrypt(text, key):

    alphabets = "abcdefghijklmnopqrstuvwxyz"

    text = text.lower()

    key = key.lower()

    key_index = 0

    cipher = ""

    for char in text:

        if char in alphabets:

            p = alphabets.index(char)

            k = alphabets.index(key[key_index % len(key)])

            c = (p + k) % 26

            cipher += alphabets[c]

            key_index += 1

        else:

            cipher += char

    print(f"Encrypted Text = {cipher.upper()} ")


def decrypt(text, key):

    alphabets = "abcdefghijklmnopqrstuvwxyz"

    text = text.lower()

    key = key.lower()

    key_index = 0

    decrypt_text = ""

    for char in text:

        if char in alphabets:

            c = alphabets.index(char)

            k = alphabets.index(key[key_index % len(key)])

            p = (c - k) % 26

            decrypt_text += alphabets[p]

            key_index += 1

        else:

            decrypt_text += char

    print(f"Decrypted Text = {decrypt_text.lower()} ")


plaintext = input("Enter Plaintext: ")

key_word = input("Enter Keyword: ")

encrypt(plaintext, key_word)

encrypted_text = input("Enter Encrypted Text: ")

decrypt(encrypted_text, key_word)
