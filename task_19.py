n = [1, 2, 3, 4, 5]
k = 8 % len(n)
new_list = list()

for i in range(len(n)):
    if k + i < len(n):
        new_list.insert(k + i, n[i])
    else:
        new_list.insert(k + i - len(n), n[i])

print(new_list)
