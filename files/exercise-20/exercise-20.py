# Exercise number 20 - Python Workout 50 essential exercises book
# Author: Barrios Ramirez Luis Fernando
# Language: Python3 3.10.2 64-bit on Mac M1


def wordcount(file_name):

    file_counts = {
        "chars": 0,
        "words": 0,
        "lines": 0,
    }

    unique_words = set()
    

    with open(file_name) as file:
        for line in file.readlines():
            file_counts["chars"] += len(line)
            file_counts["words"] += len(line.split())
            file_counts["lines"] += 1
            unique_words.update(line.split())

    for count_v, nums in file_counts.items():
        print(f"{count_v} - {nums}")

wordcount("wcfile.txt")
    





    





