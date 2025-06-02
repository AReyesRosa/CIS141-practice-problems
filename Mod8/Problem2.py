'''
#2. Write a Python program that allows users to log their hiking trips. The program
should:
- Use a while loop to repeatedly ask for a hike name and distance in miles
- Save each entry to hiking_log.txt (each hike on a new line)
- When the user presses 0, exit the loop & print the contents of hiking_log.txt
'''
# opens the file to overwrite making it empty
with open("hiking_log.txt", "w")as file:
    hiking_log = {}

# Opens the file in append node to add new entries, without overwriting.
with open("hiking_log.txt", "a") as file:
    while True:
        name = input("What is the name of the hike? (Enter 0 to exit): ")
        if name == "0":
            break
        distance = input("What is the distance in miles? (Enter 0 to exit): ")
        if distance == "0":
            break
        # Write the hike name and distance to the file
        file.write(f"{name} - {distance} miles\n")
# after exiting the loop, read print contents of the file.write
print("\nHiking Log Entries:")
with open("hiking_log.txt", "r") as file:
    for line in file:
        print(line.strip())
