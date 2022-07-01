# Exercise number 22 - Python Workout 50 essential exercises book
# Author: Barrios Ramirez Luis Fernando
# Language: Python3 3.10.2 64-bit on Mac M1

import csv
    
def passwd_to_csv(passwords, output_file):
    results = []
    with open(passwords) as file_pass, open(output_file, "w") as file_out:
        infile = csv.reader(file_pass, delimiter=":")
        outfile = csv.writer(file_out, delimiter="\t")
        for record in infile:
            if len(record) > 1:
                outfile.writerow((record[0], record[2]))



passwd_to_csv("exer-22-data.txt", "output_data.csv")




