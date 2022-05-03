# Exercise 6 : Pig Latin sentence

Same logic than the previous exercise, but this time, translate a __series of English words into Pig Latin__ 

Bases on the "secret" language in English speaking countries. 

The rules for translating words (and sentences) from English into Pig Latin are quite simple:

* IF the word begins with a vowel (a, e, i, o or u), add "way" to the end of the word.
    * So "air" becomes "airway" and "eat" becomes "eatway".
* IF the word begins with any other letter,
    * then we take the fisrt letter, put it on the end of the word, and then add "ay".
    * Thus, "python" becomes "ythonpay", and "computer" becomes "omputercay"

## For this excercise
Write a function (pl_sentence) that takes a string containing several words, separated by spaces, assumed to be an English sentence.
The function should print the output on a single line, rather than with easch word on a separate line.