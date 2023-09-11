string = input("Enter a string: ")

unique_chars = dict()
output_string = ""

char_list = string.split()

for char in char_list:
    if char in unique_chars:
        unique_chars[char] += 1
        output_string += f"{char}_{unique_chars[char]} "
    else:
        unique_chars[char] = 0
        output_string += char + " "

print(output_string)
