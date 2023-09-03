room_1 = int(input("Enter number of desks in room 1: "))
room_2 = int(input("Enter number of desks in room 2: "))
room_3 = int(input("Enter number of desks in room 3: "))

total_desks = 0

total_desks += room_1 // 2 + room_1 % 2
total_desks += room_2 // 2 + room_2 % 2
total_desks += room_3 // 2 + room_3 % 2

print(total_desks)
