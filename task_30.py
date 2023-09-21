a1 = int(input("Enter first element: "))
d = int(input("Enter d: "))
n = int(input("Enter number of elements: "))

progression = [a1 + i * d for i in range(n)]
print(*progression)
