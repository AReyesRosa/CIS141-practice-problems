'''5. A store charges $5 for shipping on any order under $50. If the order amount is $50 or more, shipping is free.
Ask the user for the order total and print the total cost, including shipping.'''

shipping = 5
order = int(input("What is your total?: "))
if order < 50:
    total = order + shipping
    print("Your total with shipping is: $", total)
else:
    print("Your total without shipping is: $", order)
