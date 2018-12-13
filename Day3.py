# Advent of Code: Day 3
# Cutting Fabric

# Part 1: Overlapping Cuts
corners, cuts = [], []

# Read each line and extract the starting coordinates and cut size
# Corners - top left corner of a cut
# Cuts - dimensions of a cut
with open("day3input.txt", 'r') as data:
    for line in data:
        l = line.rstrip('\n').split('@ ')[-1].split(": ")
        corners.append( [int(n) for n in l[0].split(',')] )
        cuts.append( [int(n) for n in l[-1].split('x')] )
        print(l, corners[-1], cuts[-1])
        
# Use a 1000x1000 array to represent the fabric.
fabric = [[0 for i in range(1000)] for j in range (1000)]

# Calculate the "bounding box" of the cuts, the minimum rectangle that surrounds all the cuts given.
# This is not required for the solution, but it gives an idea of how much of the fabric is being used.
fabricx = max([cr[0] for cr in corners]) - min([cr[0] for cr in corners])
fabricy = max([cr[1] for cr in corners]) - min([cr[1] for cr in corners])

print("Bounding box of cuts: {} x {}".format(fabricx, fabricy))
print(cuts[0])

# Iterate over the rectangles and add 1 to each space to represent a cut.
for c in range(len(corners)):
    cr, ct = corners[c], cuts[c]
    for i in range(ct[0]):
        for j in range(ct[1]):
            fabric[cr[0]+i][cr[1]+j] += 1    

# Count the number of spaces that have more than 1 cut.
doublecut = 0
for i in range(1000):
    for j in range(1000):
        if fabric[i][j] >= 2:
            doublecut += 1

print("Number of spaces with multiple cuts: ", doublecut)

# Part 2: Finding the rectangle with no overlaps
for c in range(len(corners)):
    cr, ct = corners[c], cuts[c]
    # Compares the sum of the number of cuts in the rectangle to the area of the rectangle.
    # For a rectangle with only single cuts, these numbers should be identical.
    if ( sum( [sum(fabric[i][cr[1]:cr[1]+ct[1]]) for i in range(cr[0], cr[0]+ct[0])] ) == ct[0]*ct[1] ):
        # Claim ID starts at 1
        print("Rectangle with single cuts only found. Claim number:", c+1)
