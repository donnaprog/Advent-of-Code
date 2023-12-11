import re
from itertools import groupby

# Read data
puzzle_input = open("../input/puzzle_input_day_5.txt", "r").read().split("\n")[0:-1]
map_info = [list(g) for k, g in groupby(puzzle_input, key=bool) if k][1:]
seeds = re.findall('\d+', puzzle_input[0])


# Part 1
def get_numbers(info):
    nrs_lists = []
    for entry in info[1:]:
        nrs_lists.append([int(i) for i in entry.split(' ')])
    return nrs_lists


def source_to_dest(nrs_lists, source_nr):
    dest_nr = -1
    for nrs_list in nrs_lists:
        if nrs_list[1] <= source_nr < nrs_list[1] + nrs_list[2]:
            dest_nr = source_nr + (nrs_list[0] - nrs_list[1])
        else:
            continue
    if dest_nr == -1:
        dest_nr = source_nr
    return dest_nr


nrs_dict = {info[0].split(' ')[0]: get_numbers(info) for info in map_info}
cats = ['seed', 'soil', 'fertilizer', 'water', 'light', 'temperature', 'humidity', 'location']

new_locations = []
for source in seeds:
    for i in range(len(cats) - 1):
        mapping_name = cats[i] + '-to-' + cats[i + 1]
        dest = source_to_dest(nrs_dict[mapping_name], int(source))
        source = dest
    new_locations.append(source)

print(min(new_locations))


# Part 2
def dest_to_source(nrs_lists, dest_nr):
    source_nr = -1
    for nrs_list in nrs_lists:
        if nrs_list[0] <= dest_nr < nrs_list[0] + nrs_list[2]:
            source_nr = dest_nr + (nrs_list[1] - nrs_list[0])
        else:
            continue
    if source_nr == -1:
        source_nr = dest
    return source_nr


seed_range_starts = seeds[0::2]
seed_range_lens = seeds[1::2]
seed_range_ends = [int(seed_range_starts[i]) + int(seed_range_lens[i]) for i in range(len(seed_range_starts))]

cats_rev = cats[::-1]
min_location = 1000000000
for dest in range(20300000, 20400000):
    location = dest
    for i in range(len(cats) - 1):
        mapping_name = cats_rev[i + 1] + '-to-' + cats_rev[i]
        source = dest_to_source(nrs_dict[mapping_name], int(dest))
        dest = source
    if any([int(seed_range_starts[i]) <= source < int(seed_range_ends[i]) for i in range(len(seed_range_starts))]):
        min_location = min(min_location, location)

print(f'Location: {min_location}')
