# RANDOM PASSWORD GENERATOR (HARD AND UNSAFE WAY):

import random as rand
import string

def get_characters() -> str:
    characters:str = (string.ascii_lowercase + string.ascii_uppercase + string.digits + string.hexdigits)
    return characters

def get_random_password(length:int) -> str:
    password:str = ''.join(rand.choice(get_characters()) for char in range(length))
    return password

#get_random_password(int(input("Write the password length here: ")))


###################################################



# RANDOM TOKEN GENERATOR (IN A VERY SHORT AND SAFER WAY):
import secrets

def get_secret_token(length:int):
    return secrets.token_hex(length)
print(get_secret_token(int(input("Write your token length here: "))))
