def encrypt(key, text):

    alphabets = "abcdefghijklmnopqrstuvwxyz"

    text = text.lower().replace(" ", "")

    if len(text) % 2 != 0:

        text += 'x'

    cipher = ""

    for i in range(0, len(text), 2):

        p1 = alphabets.index(text[i])

        p2 = alphabets.index(text[i + 1])

        c1 = (key[0][0] * p1 + key[0][1] * p2) % 26

        c2 = (key[1][0] * p1 + key[1][1] * p2) % 26

        cipher += alphabets[c1] + alphabets[c2]

    print(f"Encrypted Text = {cipher.upper()}")  # output in uppercase


print("Enter 2 * 2 Key Matrix: ")

key_val = list(map(int, input("Key Values: ").split()))

key = [
    [key_val[0], key_val[1]],

    [key_val[2], key_val[3]]
]

plaintext = input("Enter text to encrypt: ")

encrypt(key, plaintext)
