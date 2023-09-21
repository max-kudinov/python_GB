k = int(input("Enter k: "))

friendly_dict = dict()

for i in range(2, k):
    div_sum = 1

    for j in range(2, i // 2 + 1):
        if i % j == 0:
            div_sum += j

    friendly_dict[i] = div_sum

repeats = list()
for num, value in friendly_dict.items():
    if (
        friendly_dict[num] == value
        and value in friendly_dict
        and friendly_dict[value] == num
        and num != value
        and (value, num) not in repeats
    ):
        repeats.append((num, value))
        print(num, value)
