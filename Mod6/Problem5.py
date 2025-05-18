'''5. Create a list of integers. 
Use a loop to build a new list where each element
is the square of the corresponding element in the
original list. Print the new list.'''

numbers = [1,2,3,4,5,6,7]
numbers_squared = []

for element in numbers:
    numbers_squared.append(element ** 2)
print(numbers_squared)
