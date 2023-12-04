import re

with open('../input/puzzle_input_day_1.txt', 'r') as f:
    puzzle_input = f.readlines()

text_to_number_dict = {'one': '1',
                       'two': '2',
                       'three': '3',
                       'four': '4',
                       'five': '5',
                       'six': '6',
                       'seven': '7',
                       'eight': '8',
                       'nine': '9'
                       }

calibration_values = []
for line in puzzle_input:
    digits_found = re.findall(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))', line)
    digits = []
    for digit in digits_found:
        if digit in text_to_number_dict.keys():
            digits.append(text_to_number_dict[digit])
        else:
            digits.append(digit)

    if len(digits) == 1:
        calibration_value = int(digits[0] + digits[0])
    elif len(digits) > 1:
        first_digit, last_digit = digits[0], digits[-1]
        calibration_value = int(first_digit + last_digit)
    else:
        continue
    calibration_values.append(calibration_value)

sum(calibration_values)
