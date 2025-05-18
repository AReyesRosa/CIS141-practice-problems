'''4.  Create a list of integers. 
Write code that counts how many numbers 
are positive and how many are negative,
then print both counts.'''

integers = [100,200,300,400,5,-33,45,-366]
positive_count = 0
negative_count = 0
for numbers in integers:
    if numbers > 0:
        positive_count += 1
    elif numbers < 0:
        negative_count += 1
        
print("Positive Numbers: ", positive_count)
print("Negative Numbers: ", negative_count)
