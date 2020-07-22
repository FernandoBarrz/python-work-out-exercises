# Exercise number 4 - Python WorkOut
# Author: Barrios Ramirez Luis Fernando
# Language: Python3 3.8.2 64-bit


# Main function with no arguments
def hex_output():
    decimal_num = 0
    hex_num = input('Enter a hex number to convert: ')
    for power, digit in enumerate(reversed(hex_num)):
        decimal_num += int(digit, 16) * (16 ** power)
        print(decimal_num)

hex_output()



    