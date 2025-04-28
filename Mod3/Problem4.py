'''4. Prompt the user for: a word, a first index, and a last index. 
Slice the word at the indexes provided by the user and print to the screen.'''
str1 = input("Give me a word - ")
first_index = int(input("What is the first index -  "))
last_index = int(input("What is the second index - "))
word_sliced = str1[first_index:last_index]
print("the sliced word is:", word_sliced)

