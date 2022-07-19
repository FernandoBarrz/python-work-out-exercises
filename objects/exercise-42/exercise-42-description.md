# Exercise 42 : FlexibleDict

## For this excercise

Implement a _subclass_ of _dict_ (data structure class), which I call __FlexibleDict__.
* Dics keys are Python Objects, and as such are identified with a type.
    * Ej. key 1 (an integer) store a value, then you can´t use key '1' (a string) to retrieve that value.
    * This class will allow for this.
        * If it doesn't find the user's key, it will try to convert the key to both str and int before giving up; for example. (It cast values).


 