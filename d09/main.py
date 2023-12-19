import operator

result_part_1 = 0
result_part_2 = 0

def process_alg(numbers):
    # We store the last value given as it needs to be added
        # to the result
        prediction_for_line = numbers[-1]

        # We loop until the pyramid is complete,
        # or the last number of the level is zero
        # which means, we can extrapolate the history
        # Think of a curve, the tangent now is 0
        while len(numbers) > 0 and len(set(numbers)) != 1:
            # we need to calculate the next level of the pyramid
            # which is the differnce of all the elements with the next
            numbers = list(map(operator.sub, numbers[1:], numbers[:-1]))

            # For the prediction, we always take the last number 
            # in the level
            prediction_for_line += numbers[-1]

        return prediction_for_line

with open('input.txt', 'r') as file:
    for line in file:
        numbers = list(map(int, line.split()))
        result_part_1 += process_alg(numbers)
        result_part_2 += process_alg(numbers[::-1])
        
print('[part 1]', result_part_1)
print('[part 2]', result_part_2)


