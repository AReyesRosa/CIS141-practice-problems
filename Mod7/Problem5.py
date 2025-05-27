'''
#5. Write a function called level_up(experience) that takes a player's experience
points and returns their new level based on these rules:
* 0-99 XP → Level 1
* 100-199 XP → Level 2
* 200+ XP → Level 3

Test: level_up(50),(level_up(150),level_up(250)
Input : level_up(experience)
Output: int
Function body: takes a players exp points  and returns their new level.
'''

def level_up(experience):
    if experience < 100:
        return 1
    elif experience < 200:
        return 2
    else:
        return 3
print(level_up(50))   # Output: 1
print(level_up(150))  # Output: 2
print(level_up(250))  # Output: 3
