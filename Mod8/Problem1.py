'''
#1. Create a file called gardening_tips.txt and add at least 3 gardening tips to
it. Write a Python script that reads a file gardening_tips.txt and prints
out each tip one by one.
'''

with open("gardening_tips.txt","w") as file:
    file.write("TIP 1- Select a place in your garden, and add mulch to your soil.\n")
    file.write("TIP 2- Get seed that would bloom based on the environment.\n")
    file.write("TIP 3- Ensure seeds sprouts in pot before moving to garden.\n")
    
with open("gardening_tips.txt","r") as file:
    for line in file:
        print(line.strip())
    
    
