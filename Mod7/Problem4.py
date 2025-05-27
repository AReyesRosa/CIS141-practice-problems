'''
#4. Write a function called ferry_fare(age, vehicle) that calculates the Washington
State Ferry fare based on age and whether the person has a vehicle. Assume the following rates:
* Adults (19-64): $10 without a vehicle, $20 with a vehicle.
* Seniors (65+): $5 without a vehicle, $15 with a vehicle.
* Children (0-18): Free.

Test: (ferry_fare(30, True),(ferry_fare(70, False),(ferry_fare(15, True)
Input : ferry_fare(age, vehicle):
Output: int
Function body: takes a int, boolean  and returns Output: 20,Output: 5,Output: 0.
'''
'''

def ferry_fare(age, vehicle):
    if age <= 18:
        return 0
    elif 19 <= age <= 64:
        if vehicle:
            return 20
        else:
            return 10
    elif age >= 65:
        if vehicle:
            return 15
        else:
            return 5
    else:
        return 0
print(ferry_fare(30, True))   # Output: 20
print(ferry_fare(70, False))  # Output: 5
print(ferry_fare(15, True))   # Output: 0
