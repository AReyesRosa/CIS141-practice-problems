'''3. Create a list of strings.
Write code to create a new list that includes 
only the strings longer than three characters.
Print the resulting filtered list.'''

farm_animals = ["cow","chiken","goat","pig","duck","dog","cat"]
new_farm = []
for animals in farm_animals:
    if len(animals) > 3:
        new_farm.append(animals)
print(new_farm)
