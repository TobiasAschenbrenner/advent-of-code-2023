import re

file_path = 'trebuchet.txt'

word_to_digit = {
    'one': '1', 'two': '2', 'three': '3', 'four': '4',
    'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
}

total_sum = 0

def extract_numbers(line):
    numbers = []
    i = 0
    while i < len(line):
        longest_match = ''
        for length in range(5, 0, -1):
            if i + length <= len(line):
                word = line[i:i + length].lower()
                if word in word_to_digit and len(word) > len(longest_match):
                    longest_match = word_to_digit[word]
        if longest_match:
            numbers.append(int(longest_match))
        elif line[i].isdigit():
            numbers.append(int(line[i]))
        i += 1
    return numbers

with open(file_path, 'r') as file:
    for line in file:
        stripped_line = line.strip()
        digits = extract_numbers(stripped_line)

        if digits:
            combined_number = int(str(digits[0]) + str(digits[-1]))
            total_sum += combined_number

print("Total sum:", total_sum)
