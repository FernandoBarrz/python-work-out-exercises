# Exercise number 19 - Python Workout 50 essential exercises book
# Author: Barrios Ramirez Luis Fernando
# Language: Python3 3.10.2 64-bit on Mac M1


def passwd_to_dict(file_name):
    dict_pass = {}
    result = []
    with open(file_name) as file:
        for line in file:
            if not line.startswith(("_", "#")):
                result.append(line.strip())

    for i, ele in enumerate(result):
        temp_list = ele.split(":")
        dict_pass[temp_list[0]] = temp_list[2]


    print(dict_pass)




print(passwd_to_dict('passwd.txt'))
    





