# Exercise number 29 - Python Workout 50 essential exercises book
# Author: Barrios Ramirez Luis Fernando
# Language: Python3 3.10.2 64-bit on Mac M1




def join_numbers(str_nums) -> int:

    return sum(int(num) for num in str_nums.split() if num.isdigit())


print(join_numbers("10 abc 20 de44 30 55fg 40"))







