from collections import Counter
import pandas as pd

puzzle_input = open("../input/puzzle_input_day_7.txt", "r").read().split("\n")
hands, bids = [i.split(' ')[0] for i in puzzle_input], [int(i.split(' ')[1]) for i in puzzle_input]
df = pd.DataFrame(list(zip(hands, bids)), columns=['hand', 'bid'])

# Part 1
face_to_num = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}


# Get type of hand function
def get_hand_type(hand):
    counts = [tup[1] for tup in Counter(hand).most_common()]
    if counts[0] == 5:
        hand_type = 7
    elif counts[0] == 4:
        hand_type = 6
    elif counts[0] == 3 and counts[1] == 2:
        hand_type = 5
    elif counts[0] == 3:
        hand_type = 4
    elif counts[0] == 2 and counts[1] == 2:
        hand_type = 3
    elif counts[0] == 2:
        hand_type = 2
    else:
        hand_type = 1

    return hand_type


def get_char_as_num(hand, pos):
    char = hand[pos]
    if char in face_to_num.keys():
        char_as_num = face_to_num[char]
    else:
        char_as_num = int(char)
    return char_as_num


df['hand_type'] = df['hand'].apply(get_hand_type)
for position in range(5):
    df[f'char_{position}'] = df['hand'].apply(get_char_as_num, args=(position,))

df_sorted = df.sort_values(['hand_type', 'char_0', 'char_1', 'char_2', 'char_3', 'char_4'],
                           ascending=[True] * 6)
df_sorted['hand_rank'] = range(1, len(df_sorted) + 1)

print(sum(df_sorted['bid'] * df_sorted['hand_rank']))

# Part 2
face_to_num['J'] = 1


def get_hand_type_with_j(hand):
    c = dict(Counter(hand).most_common())

    if list(c.keys())[0] == 'J':
        if len(c) > 1:
            highest_count = c['J'] + list(c.values())[1]
        else:
            highest_count = c['J']
    else:
        highest_count = list(c.values())[0] + c['J']
        del c['J']

    if highest_count == 5:
        hand_type = 7
    elif highest_count == 4:
        hand_type = 6
    elif highest_count == 3 and list(c.values())[1] == 2:
        hand_type = 5
    elif highest_count == 3:
        hand_type = 4
    elif highest_count == 2 and list(c.values())[1] == 2:
        hand_type = 3
    elif highest_count == 2:
        hand_type = 2
    else:
        hand_type = 1

    return hand_type


def get_hand_type_general(hand):
    if 'J' in hand:
        hand_type = get_hand_type_with_j(hand)
    else:
        hand_type = get_hand_type(hand)

    return hand_type


df2 = df
df2['hand_type'] = df['hand'].apply(get_hand_type_general)
for position in range(5):
    df2[f'char_{position}'] = df2['hand'].apply(get_char_as_num, args=(position,))

df2_sorted = df2.sort_values(['hand_type', 'char_0', 'char_1', 'char_2', 'char_3', 'char_4'],
                             ascending=[True] * 6)
df2_sorted['hand_rank'] = range(1, len(df2_sorted) + 1)

print(sum(df2_sorted['bid'] * df2_sorted['hand_rank']))
