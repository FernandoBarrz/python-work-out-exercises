# Exercise number 15 - Python Workout 50 essential exercises book
# Author: Barrios Ramirez Luis Fernando
# Language: Python3 3.10.2 64-bit on Mac M1


rainfall = {}

def get_rainfall():

    while True:
        city_name = input("Enter a city name: ")
        if not city_name:
            break
        
        if city_name in rainfall:
            print(f'{city_name}:  {rainfall[city_name]}')

        
        new_city_rainfall = input("How much rain has fallen in the city? (in milimeters): ")
        if not new_city_rainfall:
            break
        rainfall[city_name] = float(new_city_rainfall)

        
    for city, rain in rainfall.items():
        print(f'{city}:  {rain}')


get_rainfall()

    





