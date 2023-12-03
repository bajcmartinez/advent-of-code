import re

max_cubes = {
    'red': 12,
    'green': 13,
    'blue': 14,
}

result_part_1 = 0
result_part_2 = 0

with open('input.txt', 'r') as file:
    for line in file:
        # Split the game id text from the sets
        [game, sets] = line.split(':')
        game_id = int(game.split(' ')[1])

        game_possible = True
        set_power = 1

        for color, max_color_quantity in max_cubes.items():
            max_draw_color_quantity = max([int(d_quantity) for d_quantity, d_color in re.findall(f"(\d+) ({color})", sets)])
            set_power = max_draw_color_quantity * set_power
            if max_draw_color_quantity > max_color_quantity:
                game_possible = False

        if game_possible:
            result_part_1 += game_id

        result_part_2 += set_power

print('[part 1]', result_part_1)
print('[part 2]', result_part_2)