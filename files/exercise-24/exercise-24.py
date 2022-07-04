# Exercise number 24 - Python Workout 50 essential exercises book
# Author: Barrios Ramirez Luis Fernando
# Language: Python3 3.10.2 64-bit on Mac M1



    
def reverse_lines(input_file, output_file):
    with open(input_file, "r") as readable_file, open(output_file, "w") as writeable_file:
        for line in readable_file.readlines():
            writeable_file.write(line.strip()[::-1])
            writeable_file.write("\n")

reverse_lines("data-exer-24.txt", "output-exer-24.txt")


    
            
            
            








