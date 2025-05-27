'''
#2. Write a function called is_palindrome(s) that checks whether a string is a palindrome
(reads the same forward and backward, ignoring case). The function should
returns either True or False.

Test: racecar (True), pikachu (False), Racecar(True)
Input : string(s)
Output: boolean
Function body: lowercasse s, flip s and save to new variable(flipped_s), and compare s & flipped_s
'''
def is_palindrome(s):
    lower_s = s.lower()
    flipped_s = lower_s[::-1]
    return lower_s == flipped_s
    
print(is_palindrome("pikachu"))
print(is_palindrome("racecar"))    
print(is_palindrome("Racecar"))
