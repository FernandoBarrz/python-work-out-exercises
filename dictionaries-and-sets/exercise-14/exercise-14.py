# Exercise number 14 - Python Workout Book
# Author: Barrios Ramirez Luis Fernando
# Language: Python3 3.10.2 64-bit on Mac M1

MENU = {'sandwich': 10, 'tea': 7, 'salad': 9}

def restaurant(MENU):
    total = 0
    
    while True:
        order = input("Type the name of the order: ")
        if not order:
            print(f'Your total is ${total}')
            break
        print(f"\nOrder: {order}")
        if order in MENU:
            price = MENU[order]
            total += price
            print(f"{order} costs {price}, total is {total}")
        else:
            print(f"Sorry, we are freash out of {order} today.")

restaurant(MENU)


    

    





