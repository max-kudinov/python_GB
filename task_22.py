n = int(input("Enter n: "))
m = int(input("Enter m: "))

n_set = set()
m_set = set()

for _ in range(n):
    n_set.add(int(input("Enter a number of list n: ")))

for _ in range(m):
    m_set.add(int(input("Enter a number of list m: ")))

union = n_set.intersection(m_set)

print(sorted(union))
