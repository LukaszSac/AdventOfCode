
input = open('input.txt', 'r').read()

input = sorted(list(map(int, input.split('\n')[:-1])))
a = 0
b = len(input) - 1
sum = input[a] + input[b]
while sum != 2020:
    if sum > 2020:
        b-=1
    else:
        a+=1
    sum = input[a] + input[b]
print(input[a]*input[b])