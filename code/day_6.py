puzzle_input = open("../input/puzzle_input_day_6.txt", "r").read().split("\n")
input = [string.split()[1:] for string in puzzle_input]

nr_ways_prod = 1
for i in range(len(input[0])):
    max_time = int(input[0][i])
    nr_ways = 0
    for speed in range(max_time + 1):
        dist = (max_time - speed) * speed
        if dist > int(input[1][i]):
            nr_ways += 1
    nr_ways_prod *= nr_ways

print(nr_ways_prod)

# Part 2
max_time = int(''.join(input[0]))
max_dist = int(''.join(input[1]))
nr_ways_2 = 0
for speed in range(max_time + 1):
    dist = (max_time - speed) * speed
    if dist > max_dist:
        nr_ways_2 += 1

print(nr_ways_2)
