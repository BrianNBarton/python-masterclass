numbers_list = []
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = [even, odd]
print(numbers)

for numbers_list in numbers:
    print(numbers_list)

    for value in numbers_list:
        print(value)