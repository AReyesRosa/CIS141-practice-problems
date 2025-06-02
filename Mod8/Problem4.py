'''
#4. Create a poll.txt file that contains a list of "yea" or "nay" votes separated
by commas. Write a program that reads the poll.txt file
Count how many votes "yea" or "nay" received and print the results.
'''
#read the votes from the file   
with open("poll.txt", "r") as file:
    content = file.read()
    
# split the content into individual votes and clean them
votes = []
for vote in content.split(","):
    cleaned_vote = vote.strip().lower()
    votes.append(cleaned_vote)
    
#Count the number of 'yea' and 'nay' votes
yea_count = votes.count("yea")
nay_count = votes.count("nay")

#print the results
print("Vote Results:")
print(f"Yea: {yea_count}")
print(f"Nay: {nay_count}")
