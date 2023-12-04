result_part_1 = 0
result_part_2 = 0

numbers_by_line = []
symbols_by_line = []
processed = {}

with open('input.txt', 'r') as file:
    matrix = [list(line.strip()) for line in file.readlines()]

    def find_number_from_loc(y, x):
        # already processed
        if y in processed and x in processed[y]:
            return 0

        processed[y] = {
            x: True
        }
        digits = [matrix[y][x]]
        stop_left = False
        stop_right = False
        digit_dx = 1
        while True:
            if x+digit_dx < len(matrix[y]) and matrix[y][x + digit_dx].isdigit() and not stop_right and not (y in processed and x + digit_dx in processed[y]):
                digits.append(matrix[y][x + digit_dx])
                processed[y][x + digit_dx] = True
            else:
                stop_right = True

            if x-digit_dx >= 0 and matrix[y][x - digit_dx].isdigit() and not stop_left and not (y in processed and x - digit_dx in processed[y]):
                digits.insert(0, matrix[y][x - digit_dx])
                processed[y][x - digit_dx] = True
            else:
                stop_left = True

            if stop_right and stop_left:
                break
            digit_dx += 1

        return int(''.join(digits))

    for row_idx in range(len(matrix)):
        # search for symbols line by line
        for col_idx in range(len(matrix[row_idx])):
            if not (matrix[row_idx][col_idx].isdigit() or matrix[row_idx][col_idx] == '.'):
                gear_ratio = 1
                gear_count = 0
                for dy in [-1, 0, 1]:
                    for dx in [-1, 0, 1]:
                        if matrix[row_idx+dy][col_idx+dx].isdigit():
                            adj_number=find_number_from_loc(row_idx+dy, col_idx+dx)
                            result_part_1+=adj_number
                            if adj_number > 0:
                                gear_count+=1
                                gear_ratio*=adj_number
                if gear_count > 1:
                    result_part_2+=gear_ratio


print('[part 1]', result_part_1)
print('[part 2]', result_part_2)