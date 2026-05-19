alphabets = "abcdefghijklmnopqrstuvwxyz"


def encrypt(text):

    encrypted_text = ""

    for char in text:

        if char in alphabets:

            old_pos = alphabets.index(char)

            new_pos = (old_pos + 3) % 26

            encrypted_text += alphabets[new_pos]
        else:

            encrypted_text += char

    # encrypted output in uppercase
    print(f"encrypted text ={encrypted_text.upper()} ")


def decrypt(text):

    decrypted_text = ""

    for char in text:

        if char in alphabets:

            old_pos = alphabets.index(char)

            new_pos = (old_pos - 3) % 26

            decrypted_text += alphabets[new_pos]
        else:

            decrypted_text += char

    # decrypted output in lowercase
    print(f"decrypted text ={decrypted_text.lower()}")


plaintext = input("Enter Plain Text: ")

plaintext_input = plaintext.lower()

encrypt(plaintext_input)

ciphertext = input("Enter Cipher Text: ")

ciphertext_input = ciphertext.lower()

decrypt(ciphertext_input)
