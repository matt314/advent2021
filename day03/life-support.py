# Find life support values

# function to find most common value at a place
def most_common_bit(list_in, place):
  ones = 0
  zeros = 0
  for line in list_in:
      if int(line[place]) == 1:
        ones += 1
      else:
        zeros += 1

  print(f"ones: {ones}, zeros: {zeros}, len {len(list_in)}")

  if ones < zeros:
    return 0
  else:
    return 1

def least_common_bit(list_in, place):
  ones = 0
  zeros = 0
  for line in list_in:
      if int(line[place]) == 1:
        ones += 1
      else:
        zeros += 1

  print(f"ones: {ones}, zeros: {zeros}, len {len(list_in)}")

  if ones < zeros:
    return 1
  else:
    return 0

# function to prune list based on most common bit
def prune_list(list_in, place, value):
  list_in[:] = (state for state in list_in if int(state[place]) == value)

  # for idx, line in enumerate(list_in):
  #   state = line.strip()
  #   if int(state[place]) != value:
  #     print(f"del {list_in[idx]}, {idx}")
  #     del(list_in[idx])
  #   else:
  #     print(f"keep {list_in[idx]}, {idx}")


with open('input.txt', 'r') as inputfile:
    o2 = inputfile.readlines()
    co2 = list(o2) #inputfile.readlines()


# Main loop to parse directions
diag_fields = 12
bitno = 0

print("pruning o2")
while len(o2) != 1:
  # print(o2)
  # print(most_common_bit(o2, bitno))
  prune_list(o2, bitno, most_common_bit(o2, bitno))
  bitno += 1

bitno = 0
print("pruning co2")
while len(co2) != 1:
  # print(co2)
  # print(least_common_bit(co2, bitno))
  prune_list(co2, bitno, least_common_bit(co2, bitno))
  bitno += 1

print(o2)
print(co2)
print(f"o2: {int(o2[0], 2)}, co2: {int(co2[0], 2)}, product: {int(o2[0], 2) * int(co2[0], 2)}")