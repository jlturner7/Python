#  Find the most common character in this sentence
#  Sentence = "This is a common interview question"

#  Module for "pretty printing"
from pprint import pprint

Sentence = "This is a common interview question"
list = []

#  Create list from string
for letters in Sentence:
    list.append(letters)

#  Count charaters in list
charDict = {}
i = 0
count = {char: list.count(char) for char in list}

#  Create dictionary of characters and their number occurrences in the string
charDict[count.get(list[i])] = count

#  Test to see which key has the highest value (character with most occurrences)
mostChar = max(charDict, key=lambda x: charDict[x])

# mostChar = max(zip(charDict.values(), charDict.keys()))[1]

pprint(charDict.values(), width=1)
print(mostChar)
