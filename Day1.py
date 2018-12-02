# Advent of Code: Day 1
# Frequency Calibration

# Part 1: Given an input of frequency drifts, what is the resulting frequency from a starting frequency of zero?
with open("day1input.txt", 'r') as data:
    print("Resulting Frequency:", sum([int(line.rstrip('\n')) for line in data]))

#For a one-line solution:
print("Resulting Frequency:", sum([int(line.rstrip('\n')) for line in open("day1input.txt", 'r')]))



# Part 2: The series of frequency drifts repeats. Which frequency is the first to repeat twice?
freq_drifts = [int(line.rstrip('\n')) for line in open("day1input.txt", 'r')]
freq_total = [sum(freq_drifts[0:i+1]) for i in range(len(freq_drifts))]
drift = sum(freq_drifts)

# Check once to see if any frequencies are repeated on the first run of the sequence
for n in range(len(freq_total)):
    if freq_total.count(n) > 1:
        print("Repeated Frequency:", n)


n_drifts, freq_repeat = 0, 0
for i in range(len(freq_total)):
    for j in range(i+1, len(freq_total)):
        if ((freq_total[i]-freq_total[j])%drift == 0):
            print("{} drifts to {} in {} cycles".format(freq_total[i], freq_total[j], (freq_total[i]-freq_total[j])/drift))


'''
offset = 0
HasRepeated = False
while(not HasRepeated):
    print("Looping...")
    offset += freq_total[-1]
    for i in range(len(freq_total)):
        if (offset+freq_total[i] in freq_total):
            print("Repeated Frequency:", offset+n)
            HasRepeated = True
'''