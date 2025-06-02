'''
#3. Create a text file called song_lyrics.txt and copy the lyrics of a song into
it. Write a Python program that:
- Reads the file
- Requests 5 inputs from the user: 5 words the user would like to count the frequency of
- Counts how many times each word appears
- Creates a dictionary of the words and their counts
- Print the dictionary to the console
'''
import string

# Step 1: Read the lyrics from the file
with open("song_lyrics.txt", "r") as lyrics_file:
    lyrics_text = lyrics_file.read()

    
# Step 2: make lyrics lower case and remove punctuation and split the lyrics into words
lyrics_text = lyrics_text.lower()
translator = str.maketrans('', '', string.punctuation)
clean_lyrics = lyrics_text.translate(translator)
lyrics_words = clean_lyrics.split()


# Step 3: Get 5 words from the user
search_words = []
for i in range(5):
    word = input(f"Enter word {i+1} to search: ").strip().lower()
    search_words.append(word)

# Step 4: Count the frequency of each search word
word_counts = {}
for word in search_words:
    count = lyrics_words.count(word)
    word_counts[word] = count

# Step 5: Print the dictionary of word counts
print("\nWord Frequencies:")
for word, count in word_counts.items():
    print(f"{word}: {count}")
