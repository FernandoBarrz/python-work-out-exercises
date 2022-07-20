# Exercise 45 : Zoo

## For this excercise
* Create a __Zoo__ class, It will contain _cage_ objects, and they in turn will contain animals. It will support the following operations:
    * Given a zoo _z_, we should be able to print all of the cages (with their ID numbers) and the animals inside simply by invoking _print(z)_.
    * We should be able to get the animals with a particular color by invoking the mathod __z.animals_by_color__. For example, we can get all of the black animals by invoking __z.animals_by_color("black")__. The result should be a list of _Animal_ objects.
    * We should be able to get the animals with a particular number of legs by invoking __z.animals_by_legs__. For example, we can get all the four-legged animals by invoking __z.animals_by_legs(4)__. The result should be a list of Animals objects.
    * Finallly, we have a potential donor to our zoo who wants to provide socks for all of the animals. Thus, we need to be able to invoke __z.number_of_legs()__ and get a count of the total number of legs for all animals in our zoo.

```python
z = Zoo()
z.add_cages(c1, c2)
print(z)
print(z.animals_by_color('white'))
print(z.animals_by_legs(4))
print(z.number_of_legs())

```
* A new Cage instance will have a unique ID number.
Define a '_ _ repr _ _' method so that printing a cage prints not just the cage ID, but also the animals it contains.




 