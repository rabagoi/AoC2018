# Advent of Code: Day 7
# Sleigh Instructions

# Part 1: Getting steps in order

# Simple class that represents a step
class Step():
    def __init__(self, name):
        self.name = name
        self.prereqs = []

# Create a list of the steps, A through Z.
steps = [Step(name=chr(65+i)) for i in range(26)]

with open("day7input.txt", 'r') as data:
    for line in data:
        l = line.split()
        steps[ord(l[7])-65].prereqs.append(l[1])


# print([steps[i].name for i in range(26)])
for i in range(26):
    s = steps[i]
    s.prereqs.sort()
    #print(s.name, s.prereqs, '\n', sep='\n')


step_order = ""

# Loops over the steps until all prerequisites all steps have been used.
while False in ([s.name in step_order for s in steps]):
    for i in range(26):
        # If a step can be performed, add it to the step order and remove it from the prerequisites of the other steps.
        if steps[i].prereqs == [] and steps[i].name not in step_order:
            step_order += steps[i].name

            for j in range(26):
                p = steps[j].prereqs
                if steps[i].name in p:
                    del p[ p.index(steps[i].name) ]

            # If a step is performed, restart from the beginning of the loop to ensure alphabetical order.
            break
                    
print ("Final Step Order: ", step_order, len(step_order))