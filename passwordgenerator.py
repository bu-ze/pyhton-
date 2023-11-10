#import string and random modules
import string
import random

#define function 
def gen_password(length, upper, symbols, numbers):
    #create a string of possible characters
    possible =''
    if upper:
        possible += string.ascii_uppercase
    if symbols:
        possible += string.punctuation
    if numbers:
        possible += string.digits  
    # create password
    password = ''
    for i in range (length):
        password += random.choice(possible)
    return password

print(gen_password(10, True, True, True))