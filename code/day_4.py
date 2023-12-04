import re

with open('../input/puzzle_input_day_4.txt', 'r') as f:
    puzzle_input = f.readlines()


def find_number_of_winning_nrs(card):
    split = card.split('|')
    winning_numbers = set(re.findall('\d+', split[0])[1:])
    my_numbers = set(re.findall('\d+', split[1]))
    len_overlap = len(winning_numbers & my_numbers)
    return len_overlap


# Part 1
nr_points = 0
for card in puzzle_input:
    winning = find_number_of_winning_nrs(card)
    if winning == 0:
        continue
    else:
        nr_points += 2 ** (winning - 1)

print(nr_points)

# Part 2
card_count = {key: 1 for key in re.findall('Card\s+(\d+):', ''.join(puzzle_input))}
total_nr_cards = 0
for card_nr in card_count.keys():
    total_nr_cards += card_count[card_nr]
    card = puzzle_input[int(card_nr) - 1]
    winning = find_number_of_winning_nrs(card)
    if winning == 0:
        continue
    while card_count[card_nr] != 0:
        for i in range(winning):
            card_count[str(int(card_nr) + i + 1)] += 1
        card_count[card_nr] -= 1

print(total_nr_cards)
