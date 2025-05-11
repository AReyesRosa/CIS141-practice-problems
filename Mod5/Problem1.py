#1. Prompt the user for a positive integer n. Use a while loop to sum all the integers from 1 up to n. Print the final sum.

n = int(input("Give me a positive number: "))

if n <= 0:
        print("The number has to be positive!!")
else:
    total = 0
    i = 1
        
    while i <= n:
        total += i
        i += 1
    print("The sum of all intergers is: ", total)
