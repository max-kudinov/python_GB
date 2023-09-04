n = int(input("Enter n: "))

power = 1
num = 1

while num < n:
    print(num)
    num = 2 ** power
    power += 1
