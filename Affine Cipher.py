# based on E(x) = (ax + b) % 26
#          D(y) = (a_inverse(y - b)) % 26

alphabets = "abcdefghijklmnopqrstuvwxyz"

a_valid = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]

a = int(input("Enter a(coprime with 26): "))

if a not in a_valid:

    print("⚠️  Error: A is not coprime with 26,enter valid value")

    exit()

b = int(input("Enter b: "))

a_inv = 0

for i in range(26):
    if (a * i) % 26 == 1:
        a_inv = i
        break


def encrypt(text):

    encrypted_text = ""

    for char in text:

        if char in alphabets:

            x = alphabets.index(char)

            e = ((a * x) + b) % 26

            encrypted_text += alphabets[e]

        else:

            encrypted_text += char

    print(f"Encrypted Text = {encrypted_text.upper()}")  # output in uppercase


def decrypt(text):

    decrypted_text = ""

    for char in text:

        if char in alphabets:

            y = alphabets.index(char)

            d = (a_inv * (y - b)) % 26

            decrypted_text += alphabets[d]

        else:

            decrypted_text += char

    print(f"Decrypted Text: {decrypted_text.lower()}")  # output in lower case


plain_text = input("Enter Plain Text: ").lower()

encrypt(plain_text)

encrypted_text = input("Enter Encrypted Text: ").lower()

decrypt(encrypted_text)
