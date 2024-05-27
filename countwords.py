# Counting Pattern using Dictionaries.

# In this problem --> We want to count the number of words in the given text - we will use a dict to track the count of each word

counts = dict() # set up a empty dict
print("Enter a line of text: ") # ask for user input of texts that is needed to be counted
line = input('')

words = line.split() # split the words into lists, each word is stored in a list with no whitespaces

print('Words:', words) # track the words

print("Counting....")

for word in words: # run a for loop to add them into dict
    counts[word] = counts.get(word, 0) + 1 # each element is added into a dict with it's count.
print('Counts', counts) # print the output
