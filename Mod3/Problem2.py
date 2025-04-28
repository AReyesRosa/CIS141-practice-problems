''' 2. Prompt the user for their name and their age. Calculate their age next year.
Use string concatenation to print "Hello, <name>! You are <age1> years old.
Next year, you will be <age2> years old."'''

what_name = input("What is your name? ")
what_age = int(input("What is your age? "))

age1 = str(what_age)
age2 = str(what_age + 1)
name = str(what_name)


print("Hello, " + name + "!\nYou are " + age1 +  " years old." + "\nNext year, you will be " + age2 + " years old.")
