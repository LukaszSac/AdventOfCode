input_file = open('../input.txt', 'r')
input_line = input_file.read().split('\n')[1:-1]
one_column_width = len(input_line[0])
traversals = list()


def add_traversal(right_step, down_step):
    traversals.append({'right_step': right_step, 'down_step': down_step, 'encountered_trees': 0})


add_traversal(1, 1)
add_traversal(3, 1)
add_traversal(5, 1)
add_traversal(7, 1)
add_traversal(1, 2)

for traversal in traversals:
    right_pos = 0
    line_number = 0
    for line in input_line:
        if line_number % traversal['down_step'] != 0:
            line_number += 1
            continue
        line_number = 1
        right_pos += traversal['right_step']
        if line[right_pos % 31] == '#':
            traversal['encountered_trees'] += 1

multiplicity = 1

for traversal in traversals:
    multiplicity *= traversal['encountered_trees']

print(multiplicity)
