n = int(input("Enter n: "))

power = 0
num = 1

while num < n:
    print(num)
    num = 2 ** power
    power += 1
