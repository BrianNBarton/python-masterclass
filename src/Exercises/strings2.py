import char as char

number = input("Enter a series of numbers, use any separators you prefer: ")
separators = ""

for char in number:
    if not char.isnumeric():
        separators += char

print(separators)

values = "".join(char if char not in separators else " " for char in number).split()

print(sum(int(val) for val in values))
