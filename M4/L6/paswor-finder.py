import random
import string 

all_lowercase = string.ascii_lowercase
all_uppercase = string.ascii_uppercase
all_numbers = string.digits

all_characters = all_lowercase + all_uppercase + all_numbers

password_length = 10
password = ""

for i in range(password_length):
    password += random.choice(all_characters)

print("Password god has spoken this is your password", password)
