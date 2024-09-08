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
