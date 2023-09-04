n = int(input("Enter n: "))

max_days = 0
days = 0

for i in range(n):
    temp = int(input("Enter temp: "))
    if temp > 0:
        days += 1
        if days > max_days:
            max_days = days
    else:
        days = 0


print(max_days)
