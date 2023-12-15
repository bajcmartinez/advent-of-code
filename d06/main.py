import re

with open('input.txt', 'r') as file:
    lines = file.readlines()

times = list(map(int, re.findall(r'[\d]+', lines[0])))
distances = list(map(int, re.findall(r'[\d]+', lines[1])))

results_part_1 = 1

def calculate_race_best_times(race_time: int, race_distance: int):
    # start by holding for 1ms
    hold_for = 1
    while hold_for < race_time:
        # the total time is the time I wait plus the time it takes to go through the distance
        # the speed is the same as the amount of time I hold it for
        my_time = hold_for + (race_distance / hold_for)

        if my_time < race_time:
            # Once I found a result, I can take that index (hold_for-1), and assume that all combinations after that will fail until len()-index
            # it's a sandwich of winning numbers, only the options in the middle are winners
            # e.g. for t=7, d=9, the following winner combo is made 0,0,1,1,1,1,0,0
            # where each element is a different variation of for how long I'm holding from 0 to max race time
            return race_time - 1 - (hold_for - 1) * 2

        # increase the hold_for time
        hold_for += 1

    # should never happen unless the inputs are wrong
    return 1

for i in range(len(times)):
    race_time = times[i]
    race_distance = distances[i]
    results_part_1 *= calculate_race_best_times(race_time, race_distance)

print('[part 1]', results_part_1)

# part 2
# remove spaces from the lines to aggregate the numbers into one
merged_time_numbers = re.sub(r'[\s]+', '', lines[0])
merged_distance_numbers = re.sub(r'[\s]+', '', lines[1])

race_time = int(re.search(r'[\d]+', merged_time_numbers).group())
race_distance = int(re.search(r'[\d]+', merged_distance_numbers).group())

print('[part 2]', calculate_race_best_times(race_time, race_distance))

# 71503