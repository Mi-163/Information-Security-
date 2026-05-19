key = input("Enter Key: ").replace('j', 'i').lower()

text = input("Enter Plain Text: ").replace('j', 'i').lower()

matrix = ""

# Create Playfair matrix without duplicate letters
for char in key + "abcdefghiklmnopqrstuvwxyz":

    if char not in matrix:

        matrix += char

pairs = ""

i = 0

# Convert plaintext into pairs
while (i < len(text)):

    c1 = text[i]

    if i + 1 < len(text):

        c2 = text[i + 1]

        # If both letters are same, insert 'x'
        if c1 == c2:

            pairs += c1 + 'x'

            i += 1

        else:

            pairs += c1 + c2

            i += 2

    else:

        # Add 'x' if one letter is left
        pairs += c1 + 'x'

        i += 1

cipher = ""

# Encrypt each pair
for i in range(0, len(pairs), 2):

    pos1 = matrix.index(pairs[i])

    pos2 = matrix.index(pairs[i + 1])

    # Find row and column positions
    r1, c1 = pos1 // 5, pos1 % 5

    r2, c2 = pos2 // 5, pos2 % 5

    # Same row  move right
    if r1 == r2:

        cipher += matrix[r1 * 5 + (c1 + 1) % 5]

        cipher += matrix[r2 * 5 + (c2 + 1) % 5]

    # Same column  move down
    elif c1 == c2:

        cipher += matrix[((r1 + 1) % 5) * 5 + c1]

        cipher += matrix[((r2 + 1) % 5) * 5 + c2]

    # Rectangle rule  swap columns
    else:

        cipher += matrix[r1 * 5 + c2]

        cipher += matrix[r2 * 5 + c1]

print(f"Encrypted Text: {cipher.upper()}")
