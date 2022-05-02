# Exercise number 4 - Python WorkOut
# Author: Barrios Ramirez Luis Fernando
# Language: Python3 3.8.2 64-bit


# Main function with no arguments
def hex_output(hex_num: str) -> int:

    decimal_num = 0

    for power, digit in enumerate(reversed(hex_num)):
        decimal_num += int(digit, 16) * (16 ** power)

    return decimal_num

print(hex_output('50'))



    