import re

result = 0

with open('input.txt', 'r') as file:
    for line in file:
        digits = [char for char in line if char.isdigit()]
        result += int(digits[0] + digits[-1])

print('[part 1]', result)

# part 2
digits_map = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '0': 0
}

result = 0

with open('input.txt', 'r') as file:
    for line in file:
        digits = re.findall("(?=([0-9]|one|two|three|four|five|six|seven|eight|nine))", line)
        result += digits_map[digits[0]]*10 + digits_map[digits[-1]]

print('[part 1]', result)


