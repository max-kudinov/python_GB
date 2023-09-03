i = int(input("Enter i: "))
j = int(input("Enter j: "))

if i == j:
    print("Unsolvable")
else:
    num_carriages = i + j - 1
    print(f"There are {num_carriages} carriages")
