'''
#3. In the game Pokemon, certain types of Pokemon do extra damage to other types.
For example, water is very effective to fight fire.
Write a function called type_advantage(attacker, defender) that takes two Pokémon types as
strings and returns "Super Effective", "Not Very Effective", or "Neutral" based on
simple type effectiveness rules. Your solution only needs to work for these three sets of input:
print(type_advantage("Water", "Fire")) # "Super Effective"
print(type_advantage("Fire", "Water")) # "Not Very Effective"
print(type_advantage("Electric", "Grass")) # "Neutral"

Test: ("Water", "Fire")) # "Super Effective",("Fire", "Water")) # "Not Very Effective",("Electric", "Grass")) # "Neutral"
Input : type_advantage(attacker, defender)
Output: string
Function body: takes a string ("Water", "Fire"),("Fire", "Water"),("Electric", "Grass") and returns "Super Effective","Not Very Effective","Neutral".
'''

def type_advantage(attacker, defender):
    
    interactions = [
        ("Fire","Water","Not Very Effective"),
        ("Water","Fire", "Super Effective"),
    ]

    for atk, defn, result in interactions:
        if attacker == atk and defender == defn:
            return result
    return "Neutral"
print(type_advantage("Water", "Fire")) # "Super Effective"
print(type_advantage("Fire", "Water")) # "Not Very Effective"
print(type_advantage("Electric", "Grass")) # "Neutral"
