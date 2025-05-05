'''4. A theater wants to enforce age restrictions for movie tickets. Ask the user for their age,
and tell them whether they can see G (appropriate for under 13), PG-13 (appropriate for 13 to 17),
or R (appropriate for over 18) rated movies.'''

age = int(input("What is your age?: "))

if age >= 18:
    print ("You are able to purchase tickets for any movies ( G, PG-13, or R rated).")
elif age >= 13:
    print("You are able to purchase tickets only for G and PG-13 movies.")
else :
    print("You can only purchase tickets for G rated movies.")


    
