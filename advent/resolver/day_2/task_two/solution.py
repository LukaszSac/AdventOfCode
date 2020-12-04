import re

input_lines = open('../dayone day2input.txt', 'r').read().split('\n')[:-1]
cnt = 0
for input_line in input_lines:
    first, second, requirement, password = re.match(r'(\d+)-(\d+)\s(\w):\s(.*)', input_line).groups()
    first = int(first) - 1
    second = int(second) - 1
    if (password[first] == requirement) != (password[second] == requirement):
        cnt += 1
print(cnt)

