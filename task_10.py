num_coins = int(input("Enter a number of coins: "))

num_0 = 0
num_1 = 0

for i in range(num_coins):
    sign = int(input("Enter a sign: "))
    if sign == 0:
        num_0 += 1
    if sign == 1:
        num_1 += 1

if num_0 > num_1:
    print(num_1)
else:
    print(num_0)
