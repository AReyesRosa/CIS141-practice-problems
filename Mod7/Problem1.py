'''
#1. Write a function called count_vowels(input) that takes a string
and returns the number of vowels (a, e, i, o, u) in it.

Test: text, text_2
Input : count_vowels(input)
Output: int
Function body: takes a string text, text_2 and returns the number of vowels.
'''
def count_vowels(input_string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in input_string:
        if char in vowels:
            count += 1
    return count
text = "The competition is fierce"
text_2 = "EMANCIPATION"
print("text = ", count_vowels(text))
print("text_2 = ", count_vowels(text_2))
