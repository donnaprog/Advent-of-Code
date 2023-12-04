import re

with open('../input/puzzle_input_day_2.txt') as f:
    puzzle_input = f.readlines()

# Part 1
game_number = 1
sum_games = 0
for game in puzzle_input:
    red = list(map(int, re.findall('(\d{1,2}) red', game)))
    green = list(map(int, re.findall('(\d{1,2}) green', game)))
    blue = list(map(int, re.findall('(\d{1,2}) blue', game)))
    if all(r <= 12 for r in red) and all(g <= 13 for g in green) and all(b <= 14 for b in blue):
        sum_games += game_number
        print(f'Sum: {sum_games}')
    game_number += 1

print(sum_games)

# Part 2
power_sum = 0
for game in puzzle_input:
    red = max(list(map(int, re.findall('(\d{1,2}) red', game))))
    green = max(list(map(int, re.findall('(\d{1,2}) green', game))))
    blue = max(list(map(int, re.findall('(\d{1,2}) blue', game))))
    power = red*green*blue
    power_sum += power
