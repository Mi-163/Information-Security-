import math


def generate_keys():

    p = int(input("Enter Value of p : "))

    q = int(input("Enter Value of q: "))

    n = p * q

    phi = (p - 1) * (q - 1)

    e_vals = [e for e in range(2, phi) if math.gcd(e, phi) == 1]

    print(f"possible values of e: {e_vals}")

    e = int(input("Enter Value of e: "))

    d = pow(e, -1, phi)

    print(f"public key: e = {e}, n = {n}")

    print(f"private key: d = {d}, n = {n}")

    return (e, n), (d, n)


def encrypt(M, public_key):

    e, n = public_key

    C = pow(M, e, n)

    return C


def decrypt(C, private_key):

    d, n = private_key

    M = pow(C, d, n)

    return M


public_key, private_key = generate_keys()

M = int(input("Enter a value to encrypt: "))

Encrypted_value = encrypt(M, public_key)

print(f"Encrypted Value: {Encrypted_value}")

C = int(input("Enter a value to decrypt: "))

Decrypted_value = decrypt(C, private_key)

print(f"Decrypted Value: {Decrypted_value}")
