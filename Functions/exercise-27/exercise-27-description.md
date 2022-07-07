# Exercise 27 : Password generator

## For this excercise

Write a function, __create_password_generator__, that receives a string.
That string will return a function, which itself takes an integer argument.
Calling this function will return a password of the specified length, using
the string from which it was created.
For example:
* alpha_password = create_password_generator('abcdef')
* symbol_password = create_password_generator('!@#$%')

* print(alpha_password(5)) # efeaa
* print(alpha_password(10)) # cacdacbada

* print(symbol_password(5)) # %#@%@
* print(symbol_password(10)) # @!%%$%$%%#