



# read in line
# create array to count
# use bitwise to count?
# 

with open('input.txt', 'r') as inputfile:
    diags = inputfile.readlines()

linecount = 0

#max 12 characters per line
ones = [0] * 12
gamma = list()
episilon = list()

# Main loop to parse directions
for line in diags:
    state = line.strip()
#    print(f'{state}')
    linecount += 1

    place = 0
    while place < len(state):
        ones[place] += int(state[place])
        place += 1

print(f"Lines: {linecount}, final counts: {ones}")

place = 0
for i in ones:
  if i < linecount//2:
    gamma.append("0")
    episilon.append("1")
  else:
    gamma.append("1")
    episilon.append("0")
  place += 1

print(f"gamma bits: {gamma}")
print(f"gamma: {int(''.join(gamma), 2)}, epsilon: {int(''.join(episilon), 2)}\nproduct: {int(''.join(gamma), 2) * int(''.join(episilon), 2)}")

