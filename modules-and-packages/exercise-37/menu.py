





def menu(**kargs):
    while True:
        user_option = input("Enter a function: ")
        if not user_option:
            print("Try again: Not valid input")
            continue
        if user_option in kargs:
            return kargs[user_option]()
        else:
            print("No menu item to procced")
