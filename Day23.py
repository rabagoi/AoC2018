# Advent of Code: Day 23
# Nanobot Teleportation

# Part 1: Signal range

with open("day23input.txt", 'r') as data:
    l = data.readline()
    print (l.split(' ')[0].strip(',<pos=>').split(','))