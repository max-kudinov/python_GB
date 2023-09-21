nums = [int(num) for num in input("Enter numbers: ").split()]
range_list = [int(num) for num in input("Enter range: ").split()]

print(*[i for i in range(len(nums))
        if range_list[0] <= nums[i] <= range_list[1]])
