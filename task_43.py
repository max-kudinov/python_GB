nums = [int(num) for num in input("Enter numbers: ").split()]

repeats = dict()

for num in nums:
    if num not in repeats:
        repeats[num] = 1
    else:
        repeats[num] += 1

pairs = 0

for rep in repeats.values():
    pairs += rep // 2

print(pairs)

# print(sum([rep // 2 for rep in repeats.values()]))
