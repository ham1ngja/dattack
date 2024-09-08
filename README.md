# dattack.py

Dattack.py is a Python program that hashes a given password with SHA1 and then compares it against an extensive list of hashes of common passwords. Below is the complete source code for the program. Scroll [further down](#code-explanation) to see a line-by-line breakdown.

Disclaimer: This program is for educational purposes only. I do not condone any illegal activity. Do not use this program for anything you do not have permission to do.

```python
import hashlib


def hash(password):

    # Hash the password using SHA1
    result = hashlib.sha1(password.encode())
    return result.hexdigest()

def dictionary(hashed_password):

    # Open the hashed password list
    with open("10k-most-common.txt", 'r') as file:

        # Check every line to see if the hashes match
        for line in file:
            if hashed_password == hash(line.strip()):
                print("Password>", line.strip(),"->", hashed_password)
                print("Hash Match>", hash(line.strip()))
                exit()

    print("Password not found in list.")

password = "pass123"

# Hash the password with SHA1
hashed_password = hash(password)

# Perform the dictionary attack
dictionary(hashed_password)
```

## Code Explanation

### Password Hashing

```python
def hash(password):
    result = hashlib.sha1(password.encode())
    return result.hexdigest()
```

To begin with, we need to be able to hash passwords with SHA1. This function takes a password, hashes it, and then returns it.

### Hash

```python
password = "pass123"
hashed_password = hash(password)
```

Under normal circumstances, we would not have access to the actual password to begin with. However, given that this program was designed for learning purposes, we start off with the password, hash it, and pretend we do not know what it is.

The `hash` function will take the password, in this case, `pass123`, hash it with SHA1, return the result, and store it into `hashed_password`.

The last command in the main block is `dictionary(hashed_password)`. This calls the `dictionary()` function, and it passes along the `hashed_password`.

### Attack

In order to initiate the dictionary attack, we need to load the password list into memory. This is achieved with:

```python
with open("10k-most-common.txt", 'r') as file:
```

The password list can be found in [this GitHub repository](https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/10k-most-common.txt) Next up, we need to iterate through the list and look at each line:

```python
for line in file:
```

Finally, we need to take each line in the password list, strip any spaces or new lines, and hash it with SHA1. Then, we compare it to our hashed password:

```python
if hashed_password == hash(line.strip()):
    print("Password>", line.strip(),"->", hashed_password)
    print("Hash Match>", hash(line.strip()))
    exit()
```

If a match is found, the password is displayed, along with its hash and the hash with which it matches in the list.

```python
print("Password not found in list.")
```

If the password is not found in the list, the message above will be displayed.

## Quality Assurance

### Password in List

**Input**
```txt
password = "pass123"
```

**Output**
```
Password> pass123 -> aafdc23870ecbcd3d557b6423a8982134e17927e
Hash Match> aafdc23870ecbcd3d557b6423a8982134e17927e
```

The password was found in the list, and so the output was as expected.

### Password Not in List

**Input**
```txt
password = "metamorphosis"
```

**Output**
```
Password not found in list.
```

The password `metamorphosis` is not on the list, so it was not found.
