n = int(input("Enter n: "))
m = int(input("Enter m: "))

print(m // n + (int(not m % n == 0)))
