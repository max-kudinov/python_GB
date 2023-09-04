import math

sum = int(input("Enter a sum: "))
product = int(input("Enter a product: "))

x = (sum + math.sqrt(sum ** 2 - 4 * product)) / 2
y = (sum - math.sqrt(sum ** 2 - 4 * product)) / 2

print(x, y)
