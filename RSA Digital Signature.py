import math


def generate_hash(message):

    hash_value = 0

    for ch in message:

        hash_value = (31 * hash_value + ord(ch))

    return hash_value


p = int(input("enter p: "))

q = int(input("enter q: "))

n = p * q

phi = (p - 1) * (q - 1)

e = 3

while (math.gcd(e, phi) != 1):

    e += 2

d = pow(e, -1, phi)

print(f"public key: e = {e}, n = {n}")

print(f"private key: d = {d}, n = {n}")

message = input("enter a message: ")

hash_value = generate_hash(message)

print(f"hash_value = {hash_value}")

signature = pow(hash_value, d, n)

verified_hash = pow(signature, e, n)

if verified_hash == hash_value % n:

    print("Signature is Valid, Message is Authentic")

else:

    print("Signature is Invalid, Message is Tampered")
