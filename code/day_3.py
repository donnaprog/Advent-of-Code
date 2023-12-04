import numpy as np
import re

# Read as 2D ndarray
with open('../input/puzzle_input_day_3_example.txt') as f:
    puzzle_input = [list(line)[:-1] for line in f.readlines()]
    mat = np.array(puzzle_input)

# Find symbol coordinates
symbols = set()
symbol_locations = set()
for coords, char in np.ndenumerate(mat):
    if char != '.' and not char.isdigit():
        symbols.add(char)
        symbol_locations.add(coords)

sum_numbers = 0
for r, row in enumerate(mat):
    line = ''.join(row)
    res = re.finditer('\d+', line)
    for match in res:
        span = list(range(match.span()[0], match.span()[1]))
        box_coordinates_set = set((y, x) for y in [r-1, r, r+1] for x in list(range(span[0], span[-1] +2)))
        if symbol_locations & box_coordinates_set:
            sum_numbers += int(match.group())

print(sum_numbers)