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
for r, row in enumerate(mat):
    line = ''.join(row)
    res = re.finditer('\d+', line)
    for match in res:
        start, end = match.start(), match.end()
        box_coordinates_set = find_box_coordinates(r, start, end)
        if symbol_locations & box_coordinates_set:
            sum_numbers += int(match.group())

print(sum_numbers)
