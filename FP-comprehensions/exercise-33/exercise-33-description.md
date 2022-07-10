# Exercise 33 : Transform values

## For this excercise

Write a function, __transform_values__, that applies a function to each of the values of a dict.
* A variation of the _map_ function
Output:
* A new dict whose keys are the same as the input dict, but whose values have been transformed by the function.
* The function passed to __transform_values__ should take a single argument, the dict's value.

When your transform_values function works, you should be able to invoke it as follows:

d = {'a':1, 'b':2, 'c':3}

transform_values(lambda x: x*x, d)

The result of this call will be the following dict:
{'a': 1, 'b': 4, 'c': 9}