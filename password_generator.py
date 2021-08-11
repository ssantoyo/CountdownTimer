import random
import string

print("Hello, Welcome to Password Generator!")

pass_len = int(input("\nEnter the length of the Password: "))

#Password char data
upper = string.ascii_uppercase
lower = string.ascii_lowercase
digit = string.digits
symbols = string.punctuation

all_char = upper+lower+digit+symbols

tempPass = random.sample(all_char, pass_len)

password = ''.join(tempPass)

print(password)