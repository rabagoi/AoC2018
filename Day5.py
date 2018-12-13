# Advent of Code: Day 5
# Polymer Reactions

from math import fabs

# Part 1: Fully reacting the polymer
polymer = open("day5input.txt", 'r').readline().rstrip('\n')
newpolymer = ''

# Treat the reacted polymer like a stack, and construct it from the original polymer.
for l in range(len(polymer)):
    # Pop a letter from the stack if the incoming letter is the same kind. They react, and so neither of them remain on the stack.
    if len(newpolymer) != 0 and fabs(ord(polymer[l]) - ord(newpolymer[-1])) == 32:
        newpolymer = newpolymer [:-1]
    # Otherwise, push the letter onto the stack.
    else:
        newpolymer += polymer[l]

# Display the final polymer length, along with the tail end of the polymer.
print(newpolymer[-20:])
print("Final polymer length:", len(newpolymer))

# Part 2: Removing a letter to shorten the polymer
lengths = []
for i in range(26):
    newpolymer = ''
    # Same rules as before, but with an extra rule to ignore a particular letter.
    for l in range(len(polymer)):
        # Pop a letter from the stack if the incoming letter is the same kind. They react, and so neither of them remain on the stack.
        if len(newpolymer) != 0 and fabs(ord(polymer[l]) - ord(newpolymer[-1])) == 32:
            newpolymer = newpolymer [:-1]
        # If the letter is to be removed, do not add it onto the stack.
        elif (ord(polymer[l])-(i+65))%32 == 0:
            pass
        # Otherwise, push the letter onto the stack.
        else:
            newpolymer += polymer[l]
    
    lengths.append(len(newpolymer))

print("Shortest polymer achieved by removing unit", chr(lengths.index(min(lengths))+65) )
print("Length of shortest polymer:", min(lengths))