# This script copies a file from a source location to a destination location using low-level file operations in Python.
import os

src = input("enter source file: ")

dest = input("enter destination file: ")

fd_in = os.open(src, os.O_RDONLY)

fd_out = os.open(dest, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o644)

while (True):

    data = os.read(fd_in, 1024)

    if not data:

        break

    os.write(fd_out, data)

os.close(fd_in)

os.close(fd_out)

print("file copied successfully")
