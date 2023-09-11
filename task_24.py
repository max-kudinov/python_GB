n = 0

while n < 3:
    n = int(input("Enter a number of bushes: "))


berries = [int(input("Enter a number of berries: ")) for _ in range(n)]

max_sum = berries[0] + berries[1] + berries[2]

for i in range(1, n):
    sum = berries[i] + berries[(i + 1) % n] + berries[(i + 2) % n]
    if sum > max_sum:
        max_sum = sum

print(max_sum)
