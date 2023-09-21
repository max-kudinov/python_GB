n = int(input("Enter n: "))
n_list = [int(num) for num in input("Enter numbers: ").split()[:n]]

m = int(input("Enter n: "))
m_list = [int(num) for num in input("Enter numbers: ").split()[:m]]

print(*[i for i in n_list if i not in m_list])
