
input = open('../dayone day2input.txt', 'r')
input_line = input.read().split('\n')[1:-1]
one_column_width = len(input_line[0])
right_pos = 0
counter = 0
for line in input_line:
    right_pos += 3
    if line[right_pos%31] == '#':
        counter += 1
print(counter)