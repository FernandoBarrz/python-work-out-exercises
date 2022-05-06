# Exercise 10 : Summing anything

## For this excercise

Redifine the _mysum_ function defined in exercise-1, such that it can take any number or arguments.
* The arguments must all be of the same type and know how to respond to the + operator.
+ The result should be anew, longer sequence of the type provided by the parameters.
    * Thus, the result of mysum('abc', 'def') will be the string 'abcdef', and the result of mysum([1, 2, 3], [4, 5, 6]).
        * Will be the six-element list [1, 2, 3, 4, 5, 6]


### Note:

> Slices are forgiving and allow us to specify indexes beyong the sequence's boundaries.

> In Python, everything is considered "True" in an "if", except for "None", "False", 0. and empty collections.