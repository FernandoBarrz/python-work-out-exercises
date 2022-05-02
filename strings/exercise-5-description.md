# Exercise 5 : Pig Latin

Bases on the "secret" language in English speaking countries. 

The rules for translating words from English into Pig Latin are quite simple:

* IF the word begins with a vowel (a, e, i, o or u), add "way" to the end of the word.
    * So "air" becomes "airway" and "eat" becomes "eatway".
* IF the word begins with any other letter,
    * then we take the fisrt letter, put it on the end of the word, and then add "ay".
    * Thus, "python" becomes "ythonpay", and "computer" becomes "omputercay"

## For this excercise
Write a function (pig_latin) that takes a string as input, assumed to be an English word.
The function should return the translation of this word into Pig Latin