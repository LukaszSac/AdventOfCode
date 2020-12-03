input = open('input.txt', 'r').read()

input = sorted(list(map(int, input.split('\n')[:-1])))
left = 0
inner = 1
right = 2
desired_sum = 2020
desired_inner_sum = 2020
while input[right] < desired_sum:
    desired_inner_sum = desired_sum - input[right]
    found = False
    left = 0
    inner = right - 1
    while left < inner:
        if input[left] + input[inner] < desired_inner_sum:
            left += 1
        elif input[left] + input[inner] > desired_inner_sum:
            inner -= 1
        else:
            found = True
            break
    if found:
        break
    right += 1

print(input[left] * input[inner] * input[right])
