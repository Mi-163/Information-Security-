import hashlib

s1 = input("enter string1: ")

h1 = hashlib.sha256(s1.encode()).hexdigest()

print(f"h1(hex): {h1}")

s2 = input("enter string2: ")

h2 = hashlib.sha256(s2.encode()).hexdigest()

print(f"h2(hex): {h2}")

h1_int = int(h1, 16)

h2_int = int(h2, 16)

xor_result = h1_int ^ h2_int

bit_difference = bin(xor_result).count('1')

print(f"bit difference: {bit_difference}")
