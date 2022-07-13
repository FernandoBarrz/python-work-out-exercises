# Exercise 36 : Sales tax

## For this excercise

Implement a Python module, __freedonia.py__, It should provide a function, __calculate_tax__, that takes three arguments:
1. the amount of the purchase
2. The province in which the purchase took place
3. The hour (an integer, from 0-24) at which it happend.
The function should return the final price, as a float.
Provide a solution creating two separate files:
* The program that calls __calculate_tax__ should be in a file called __use_freedonia.py__, which uses _import_ to load the funciton

Thus, if I were to invoke: calculate_tax(500, "Harpo", 12) -> a $625 


Sales tax on purchases in Freedonia depends on where the purchase was made, as well as the time of the purchase.
Fredonia has four provinces, each of which charges its own percentage of tax:
* Chico: 50%
* Groucho: 70%
* Harpo: 50%
* Zeppo; 40%
The tax percentage is always multiplied by the hour at which the purchase was made.
    * i.e., when the 24-hour clock is 0, there's no sales tax.
    * From 12 noon until 1 p.m, only 50% (12/24) of the tax applies
    * And from 11 p.m until midnight, 95.8% (i.e., 23/24) of the tax applies.