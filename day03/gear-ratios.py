def extract_num(m, i, j):
    num, start_j = '', j
    while j >= 0 and m[i][j].isdigit():
        num = m[i][j] + num
        j -= 1
    end_j = start_j + 1
    while end_j < len(m[0]) and m[i][end_j].isdigit():
        num += m[i][end_j]
        end_j += 1
    return num, j + 1, end_j

def collect_symbols(m, i, j):
    symbols = set()
    adj = [(i-1, j), (i+1, j), (i, j-1), (i, j+1), (i-1, j-1), (i-1, j+1), (i+1, j-1), (i+1, j+1)]
    for ai, aj in adj:
        if 0 <= ai < len(m) and 0 <= aj < len(m[0]) and not m[ai][aj].isdigit() and m[ai][aj] != '.':
            symbols.add(m[ai][aj])
    return symbols

def sum_adjacent_nums(m):
    total = 0
    for i in range(len(m)):
        j = 0
        while j < len(m[0]):
            if m[i][j].isdigit():
                num, start_j, end_j = extract_num(m, i, j)
                symbols = set()
                for pos in range(start_j, end_j):
                    symbols.update(collect_symbols(m, i, pos))
                if symbols:
                    total += int(num)
                j = end_j
            else:
                j += 1
    return total

with open('gear-ratios.txt', 'r') as file:
    m = [list(line.strip()) for line in file.readlines()]

total = sum_adjacent_nums(m)
print("Sum of numbers adjacent to symbols:", total)
