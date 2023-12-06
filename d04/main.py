import math

result_part_1 = 0

copies_per_card = [1]*186

with open('input.txt', 'r') as file:
    for i, line in enumerate(file):
        [winner_numbers, my_numbers] = [set(numbers.split()) for numbers in line.split(':')[1].split('|')]
        my_winner_numbers = my_numbers.intersection(winner_numbers)
        result_part_1 += math.floor(2 ** (len(my_winner_numbers) - 1))

        for j in range(len(my_winner_numbers)):
            copies_per_card[j+i+1] = copies_per_card[j+i+1] + copies_per_card[i]


print('[part 1]', result_part_1)
print('[part 2]', sum(copies_per_card))