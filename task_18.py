list_1 = [1, 2, 4, 5]
k = 3

min_diff = abs(list_1[0] - k)
element = list_1[0]

for i in range(1, len(list_1)):
    diff = abs(list_1[i] - k)
    if diff < min_diff:
        min_diff = diff
        element = list_1[i]

print(element)
