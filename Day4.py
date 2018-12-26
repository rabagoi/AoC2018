# Advent of Code: Day 4
# Sleeping Guards

import re

# Gets the time, in minutes, from the start of 1518.
# Months part needs to be fixed.
def get_time_1518(line):
    months, days, hrs, mins = int(line[1]), int(line[2]), int(line[3]), int(line[4])
    return months*43200 + days*1400 + hrs*60 + mins

l = open("day4input.txt", 'r').readline()

print(l)

l1 = re.split(r':|-|\] | ', l.strip('[\n'))
print(l.split())
print (l1)

# Calculate number of seconds from 1518
# Sort entries
print (get_time_1518(l1))