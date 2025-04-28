''' Prompt the user for a word. Then, prompt the user for how many times they'd like that word repeated.
Use the skills you learned in this module to print the word the correct number of times.'''
str1 = input("What is a word that you would like to get repeated? ")
str2 = int(input(" How many times you would like the word to be repeated? "))
word = (str1 + ' ') * str2
print( word)
