import itertools
import math
import re

coords = {}

with open('input.txt', 'r') as file:
    nav = [*file.readline()][:-1]
    nav = [0 if i == 'L' else 1 for i in nav]

    file.readline()
    for line in file:
        data = re.findall(r'[\d|A-Z][\d|A-Z][\d|A-Z]+', line)
        coords[data[0]] = [data[1], data[2]]

curr_pos = 'AAA'
steps = 0
for direction in itertools.cycle(nav):
    curr_pos = coords[curr_pos][direction]
    steps += 1

    if curr_pos == 'ZZZ':
        break

print('[part 1]', steps)

# Part 2
curr_positions = [coord for coord in coords.keys() if coord.endswith('A')]
steps = 0

# Paying a lot of attention to the example, you can see that once we find Z for any starting point
# it starts all over again from the beginning, Z always re-leads to A.
# This is not very clear in the problem, and took me a while to find out, but without it, it's impossible to solve
# as brute forcing for 15 minutes yield no results
# so we save how many steps on each starting point until the first Z
# then we find the minimum common product to find out when they all meet at Z
step_lists = [None]*len(curr_positions)

for direction in itertools.cycle(nav):
    steps += 1

    for i in range(len(curr_positions)):
        curr_positions[i] = coords[curr_positions[i]][direction]
        if curr_positions[i].endswith('Z'):
            step_lists[i] = steps

    #  exit when we found at least one Z for each starting point
    if None not in step_lists:
        break

print('[part 2]', math.lcm(*step_lists))