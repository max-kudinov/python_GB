n = int(input("Enter quantity of watermelons: "))

mass = int(input("Enter a mass of watermelon: "))

min_mass = mass
max_mass = mass

for i in range(n - 1):
    mass = int(input("Enter a mass of watermelon: "))
    if mass < min_mass:
        min_mass = mass
    elif mass > max_mass:
        max_mass = mass

print(f"Min: {min_mass}")
print(f"Max: {max_mass}")
