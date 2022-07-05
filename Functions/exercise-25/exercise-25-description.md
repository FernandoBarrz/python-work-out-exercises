# Exercise 25 : XML generator

## For this excercise

Write a function, _myxml_, that allows you to create simple XML output.
The output from the function will always be a string.
THe first argument is the name of the tag.
THe second argument is the content for that tag.
More arguments are turned into attributes.
For example:
* myxml("foo") -> <foo></foo>
* myxml("foo", "bar") -> <foo>bar</foo>
* myxml("foo", "bar", a=1, b=2, c=3) -> <foo a="1" b="2" c="3">bar</foo>


