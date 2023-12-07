import re
from itertools import groupby

# Read data
puzzle_input = open("../input/puzzle_input_day_5_example.txt", "r").read().split("\n")[0:-1]
map_info = [list(g) for k, g in groupby(puzzle_input, key=bool) if k][1:]
seeds = re.findall('\d+', puzzle_input[0])


def get_numbers(info):
    for entry in info[1:]:
        nrs = [int(i) for i in entry.split(' ')]
    return nrs


def source_to_dest(nrs, source_nr):
    if nrs[1] <= source_nr < nrs[1] + nrs[2]:
        dest_nr = source_nr + (nrs[0] - nrs[1])
    else:
        dest_nr = source_nr
    return dest_nr


nrs_dict = {info[0].split(' ')[0]: get_numbers(info) for info in map_info}
cats = ['seed', 'soil', 'fertilizer', 'water', 'light', 'temperature', 'humidity', 'location']

for source in seeds:
    for i in range(len(cats) - 1):
        mapping_name = cats[i] + '-to-' + cats[i + 1]
        dest = source_to_dest(nrs_dict[mapping_name], int(source))
        print(source, dest)
        source = dest
    new_location = source

# print(lowest_location)