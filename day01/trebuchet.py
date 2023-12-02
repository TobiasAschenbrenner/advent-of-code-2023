import re

file_path = 'trebuchet.txt'

word_to_digit = {
    'one': '1', 'two': '2', 'three': '3', 'four': '4',
    'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
}

total_sum = 0

def extract_numbers(line):
    numbers = []
    
    pattern = r'\b(?:' + '|'.join(re.escape(word) for word in word_to_digit) + r')\b|\d'
    
    for match in re.finditer(pattern, line, flags=re.IGNORECASE):
        if match.group().lower() in word_to_digit:
            numbers.append(int(word_to_digit[match.group().lower()]))
        else:
            numbers.append(int(match.group()))
    
    return numbers

with open(file_path, 'r') as file:
    for line in file:
        stripped_line = line.strip()
        digits = extract_numbers(stripped_line)

        if digits:
            combined_number = int(str(digits[0]) + str(digits[-1]))
            total_sum += combined_number

print("Total sum:", total_sum)
