# Exercise 37 : Menu

## For this excercise

Write a new module called __menu.py__.
The module should:
* Define a function, also called _menu_
    * This function takes any number of key-value pairs as arguments.
    * Each value should be a _callable_(a function or class )
    * When invoked, the user is asked to enter some input.
        * It the user enters a string that matches one of the keyword arguments, the function associated with that keyword will be invoked, and its return value will be return to menu's caller.
        * If the user enters a string that's not one of the keywords arguments, they'll be give an error message and asked to try again.
* 