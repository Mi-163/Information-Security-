# Operating Systems & Cryptography Lab

## 📌 Overview
This repository contains a collection of scripts and programs demonstrating core concepts in cryptography, operating system-level system calls, and Linux shell scripting. 

## 📂 Repository Structure

### 1. Cryptography & Security Algorithms (Python)
Implementation of classic and modern encryption algorithms, as well as digital signatures.
* `Affine Cipher.py`
* `Caesar Cipher.py`
* `Hill Cipher Encryption.py`
* `Playfair Cipher Encryption.py`
* `RSA.py`
* `RSA Digital Signature.py`
* `Vigenere Cipher.py`
* `SHA 256.py`

### 2. Operating System Calls (C & Python)
Programs bypassing standard libraries to interact directly with the OS kernel.
* `system_calls.c`: Demonstrates process management and file metadata using `fork()`, `stat()`, `opendir()`, and `execlp()`.
* `copy file.py`: Copies contents between files using low-level file descriptors (`os.open`, `os.read`, `os.write`).
* `source.txt` / `destination.txt`: Sample text files used for system call I/O operations.

### 3. Shell Scripting (Bash)
Scripts automating Linux administrative and security tasks.
* `deny_rights.sh`: Automates the removal of execution rights.
* `list_files.sh`: Directory parsing and file listing.
* `user_login.sh`: User authentication simulation.
* `sha256.sh`: Verifies file integrity using SHA-256 checksums.

---

## 💻 Linux Permissions & ACL Reference Guide

This section serves as a quick reference for standard Linux file permissions (`chmod`) and Advanced Control Lists (`setfacl`).

### Standard File Permissions (`chmod`)

**1. Displaying & Creating**
* `ls -l`              # List files with detailed permission info
* `ls -ld mydir`       # List permissions for a directory itself
* `touch file.txt`     # Create a standard file
* `mkdir mydir`        # Create a directory

**2. Symbolic Mode (Adding/Removing Rights)**
* `chmod u+x file.txt` # Add Execute to User (Owner)
* `chmod g+w file.txt` # Add Write to Group
* `chmod o+r file.txt` # Add Read to Others
* `chmod u-x file.txt` # Remove Execute from User
* `chmod a+rwx file.txt` # Give ALL users Read/Write/Execute
* `chmod u=rwx,g=rx,o=r file.txt` # Set exact permissions explicitly

**3. Numeric (Octal) Mode**
*(4 = Read, 2 = Write, 1 = Execute)*
* `chmod 777 file.txt` # Wide open (rwxrwxrwx)
* `chmod 755 file.txt` # Standard executable/script (rwxr-xr-x)
* `chmod 644 file.txt` # Standard text file (rw-r--r--)
* `chmod 700 mydir`    # Total directory privacy (rwx------)

### Access Control Lists (ACLs)

**1. Managing Users and Groups**
* `sudo useradd student`    # Create a new dummy user
* `sudo groupadd staff`     # Create a new group
* `grep staff /etc/group`   # Verify group creation

**2. Viewing and Setting ACLs**
* `getfacl my_test_file`                # View current custom permissions
* `setfacl -m u:student:rw my_test_file`  # Grant specific user read/write
* `setfacl -m g:staff:r my_test_file`     # Grant specific group read-only

**3. Removing ACLs**
* `setfacl -x u:student my_test_file`   # Extract/remove a single specific rule
* `setfacl -b my_test_file`             # Wipe clean (remove all custom ACLs)

---
