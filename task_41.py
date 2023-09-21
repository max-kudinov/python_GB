n = int(input("Enter n: "))
nums = [int(num) for num in input("Enter numbers: ").split()[:n]]

print(len([i for i in range(1, n - 1) if nums[i - 1] < nums[i] > nums[i + 1]]))
