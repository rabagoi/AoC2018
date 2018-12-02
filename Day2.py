# Advent of Code: Day 2
# ID Checksums

# Part 1: Checksum of IDs
ID_list = []
doubles, triples = 0, 0
with open("day2input.txt", 'r') as data:
    for line in data:
        ID_list.append(line.rstrip('\n'))
        if (2 in [line.count(letter) for letter in line]):
            doubles += 1
        if (3 in [line.count(letter) for letter in line]):
            triples += 1
        
print("Checksum:", doubles*triples)

# Part 2: Locating two IDs which differ by one letter
for ID_num, ID in enumerate(ID_list):
    for nextID in ID_list[ID_num+1:]:
        diffs = 0
        for i in range(len(ID)):
            if ID[i] != nextID[i]:
                diffs += 1
                diff_index = i
        
        if diffs == 1:

            print("Difference of 1 letter found in IDs {} and {}".format(ID, nextID))
            print("Difference occurs at index {} with letters {} and {}".format(diff_index, ID[diff_index], nextID[diff_index]))
            
