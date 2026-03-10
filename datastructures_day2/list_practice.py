"""
list_practice.py

In this exercise, you will practice the most common list methods.

Write your lines of code under each comment.
"""

# create a list named 'numbers' with the integers 1 to 8
numbers = [1,2,3,4,5,6,7,8]

# add 9 to the end of the list
numbers.append(9)

# add the extension to the end of your numbers list
new_numbers = [10, 11, 12, 13, 14, 15, 16]
numbers.extend(new_numbers)

# print out an informative message that gives the number of 
# elements in the list, and then the list itself
# no hard coding! (don't count in your head and print it, 
# have the code count for you)

print("The lengths of the list is:", len(numbers))

# here is a list, can you print out how many times 'dog' occurs?
animals = ['cat', 'rat', 'mouse', 'dog', 'giraffe', 'dog']

# insert a moose at the first position of the animals list

animals.insert(0, 'moose')
print(animals)

# using the remove() method, remove 'dog' - 
# check the list - is this the behaviour you expect?

animals.remove('dog')
print(animals)

# pop out the 3rd element, what do you get?

animal = animals.pop(2)
print(animal)
print(animals)

# reverse the animal list
animals.reverse()
print(animals)


# clear the animal list, what do you get?

animals.clear()
print(animals)




