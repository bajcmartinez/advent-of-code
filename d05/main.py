import re

with open('input.txt', 'r') as file:
    lines = file.read().splitlines()

# Build a matrix of ranges and processing
ranges = []
for line in lines[2:]:
    # Add a new row for each section
    if 'map' in line:
        ranges.append([])
    else:
        if len(line) > 0:
            ranges[-1].append(list(map(int, re.findall(r'[\d]+', line))))

# Part 1
min_location = float('inf')
seed_locations = list(map(int, re.findall(r'[\d]+', lines[0]))) # the numbers on the first row are seeds

for seed_location in seed_locations:
    curr_location = seed_location
    for mapping_range in ranges:
        for mapping in mapping_range:
            destination_range = mapping[0]
            source_range = mapping[1]
            range_length = mapping[2]
            if source_range <= curr_location < source_range + range_length:
                curr_location = destination_range + curr_location - source_range
                # IMPORTANT: once you find the range, stop processing other ranges in the same map
                break
    min_location = min(min_location, curr_location)

print('part 1', min_location)

# Part 2
# The number of seeds is huge, and can't be done like we did for part 1
# Instead we have to process a new mapping with ranges of seeds going through the proceesing

min_location = float('inf')
# build a map of x1, x2 and level for each seed location, where level is 0
curr_location_ranges = [(seed_locations[i], seed_locations[i]+seed_locations[i+1], 0) for i in range(0, len(seed_locations), 2) ]

while curr_location_ranges:
    x1, x2, level = curr_location_ranges.pop()

    if level == 7:
        # we are done processing this particular location, next we can check if it's a minimum or let it be
        min_location = min(x1, min_location)
        continue

    for mapping in ranges[level]:
        destination_range = mapping[0]
        y1 = mapping[1] # source_range
        dy = mapping[2] # range_length
        y2 = y1 + dy
        transformation_diff = destination_range - y1

        # There are multiple scenarios that can occur here

        if x2 <= y1 or y2 <= x1:
            # no overlap, there's nothing to do
            continue

        if x1 < y1:
            # split the original interval at the beginning of the range
            # keep the same level so that it is processed again until the current location fits in a range
            curr_location_ranges.append((x1, y1, level))
            x1 = y1

        if x2 > y2:
            # split the original interval at the end of the range
            # keep the same level so that it is processed again until the current location fits in a range
            curr_location_ranges.append((y2, x2, level))
            x2 = y2

        # The piece that is left which fits in a range needs to be processed and sent to the next level
        curr_location_ranges.append((x1 + transformation_diff, x2 + transformation_diff, level + 1))

        # IMPORTANT: once you find the range, stop processing other ranges in the same map
        break
    else:
        # If we didn't break mean that there is no transformation to be done for this particular location, so stays as is and moves to the next level
        curr_location_ranges.append((x1, x2, level + 1))

print('part 2', min_location)