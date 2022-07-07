# Exercise number 27 - Python Workout 50 essential exercises book
# Author: Barrios Ramirez Luis Fernando
# Language: Python3 3.10.2 64-bit on Mac M1

from random import choice

def create_password_generator(chars):
    def generate_passwd(passwd_len):
        output_passwd = ''
        while len(output_passwd) <= passwd_len:
            output_passwd += choice(chars)
        return output_passwd
    return generate_passwd

alpha_password = create_password_generator("abcdef")
symbol_password = create_password_generator("!@#$%")


print(alpha_password(5))
print(alpha_password(10))

print(symbol_password(5))
print(symbol_password(10))
    