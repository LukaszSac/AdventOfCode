import re

input_lines = open('../input.txt', 'r').read().split('\n')[:-1]
cnt = 0
for input_line in input_lines:
    least, most, requirement, password = re.match(r'(\d+)-(\d+)\s(\w):\s(.*)', input_line).groups()
    if re.match(fr'^[^{requirement}]*({requirement}[^{requirement}]*[^{requirement}]*){{{least},{most}}}$', password) is not None:
        cnt += 1
print(cnt)