n = int(input("Enter a 3 digit number: "))

sum = 0
sum += n % 10
sum += n // 10 % 10
sum += n // 100

print(sum)
