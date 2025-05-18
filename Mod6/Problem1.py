'''1. Create a list of integers (you get to pick!). 
Write code to iterate through the list and calculate the sum of all even numbers. 
Print the resulting sum.'''

# list
numbers_list = [1,2,3,4,5,6,7,8,9,10]

#sliced list taking even numbers and giving the sum as long as the list does not change
print(sum(numbers_list[1:10:2]))

# or using a for loop
even_sum = 0
for num in numbers_list:
    if num % 2 == 0:
        even_sum += num
print(even_sum)
