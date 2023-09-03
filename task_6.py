ticket = int(input("Enter a 6 digit ticket number: "))

sum_1 = 0
sum_2 = 0

sum_1 += ticket // 100_000
sum_1 += ticket // 100_00 % 10
sum_1 += ticket // 100_0 % 10

sum_2 += ticket % 10
sum_2 += ticket // 10 % 10
sum_2 += ticket // 100 % 10

if sum_1 == sum_2:
    print("yes")
else:
    print("no")
