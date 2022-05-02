# Exercise #4 - Hexadecimal output

For this exercise:
* For this exercise, you need to write a function ( hex_output ) that takes a hex num-
    ber and returns the decimal equivalent. That is, if the user enters 50 , you’ll assume
    that it’s a hex number (equal to 0x50 ) and will print the value 80 to the screen. And
    no, you shouldn’t convert the number all at once using the int function, although it’s
    permissible to use int one digit at a time.

That is, if the user enters 50 , you’ll assume
that it’s a hex number (equal to 0x50 ) and will print the value 80 to the screen. And
no, you shouldn’t convert the number all at once using the int function, although it’s
permissible to use int one digit at a time.

We need to convert each digit of our decimal number, which was entered as a
string, into an integer.

We also
see that int takes two arguments. The first is mandatory and is the string we want to
turn into an integer. The second is optional and contains the number base. Since
we’re converting from hexadecimal (i.e., base 16), we pass 16 as the second argument.