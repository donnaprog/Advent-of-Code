import numpy as np
import re

# Read as 2D ndarray
with open('../input/puzzle_input_day_3.txt') as f:
    puzzle_input = [list(line)[:-1] for line in f.readlines()]
    mat = np.array(puzzle_input)

# Part 1
# Find symbol coordinates
symbols = set()
symbol_locations = set()
for coords, char in np.ndenumerate(mat):
    if char != '.' and not char.isdigit():
        symbols.add(char)
        symbol_locations.add(coords)


def find_box_coordinates(r, start, end):
    box_coords = set((y, x) for y in [r - 1, r, r + 1] for x in range(start - 1, end + 1))
    return box_coords


sum_numbers = 0
numbers = []
number_coords = []
for r, row in enumerate(mat):
    line = ''.join(row)
    res = re.finditer('\d+', line)
    line_numbers = []
    line_coords = []
    for match in res:
        line_numbers.append(int(match.group()))
        start, end = match.start(), match.end()
        line_coords.append([(r, xn) for xn in range(start, end)])
        box_coordinates_set = find_box_coordinates(r, start, end)
        if symbol_locations & box_coordinates_set:
            sum_numbers += int(match.group())
    numbers.append(line_numbers)
    number_coords.append(line_coords)

print(sum_numbers)

# Part 2
gear_locations = set()
for coords, char in np.ndenumerate(mat):
    if char == '*':
        gear_locations.add(coords)

gear_ratio_sum = 0
for gear_loc in gear_locations:
    neighbours = find_box_coordinates(gear_loc[0], gear_loc[1], gear_loc[1] + 1)
    factors = []
    for line_nr, values in enumerate(numbers):
        for pos, value in enumerate(values):
            coords = set(number_coords[line_nr][pos])
            if neighbours & coords:
                factors.append(numbers[line_nr][pos])
    if len(factors) == 2:
        gear_ratio_sum += factors[0]*factors[1]

print(gear_ratio_sum)

