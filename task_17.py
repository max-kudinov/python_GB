n = [1, 1, 2, 0, -1, 3, 4, 4]
# print(len(set(n)))

unique_numbers = list()

for i in range(len(n)):
    if n[i] not in unique_numbers:
        unique_numbers.append(n[i])

print(len(unique_numbers))
