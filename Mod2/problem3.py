'''
3. Create a program that prompts for the side lengths of a triangle 
and computes the area using Heron's formula.
(https://en.wikipedia.org/wiki/Heron%27s_formula)
'''
import math
a = int(input("Enter the first side length: "))
b = int(input("Enter the second side length: "))
c = int(input("Enter the third side length: "))

s = (a + b + c) / 2

area = (s*(s - a)*(s - b)*(s - c)) 

print(f"The area of the triangle is {math.sqrt(area):.2f}.")
