pangram = "the quick brown fox jumped over the lazy dog"
letters = sorted(pangram)
print(letters)


numbers = [2.3, 4.5, 8.7, 3.1, 9.2, 1.6]
sorted_numbers = sorted(numbers)
print(sorted)
print(numbers)
another_sorted_numbers = numbers.sort()

numbers.sort()
print(numbers)

missing_letter = sorted("The quick brown fox jumped over the lazy dog",
                        key=str.casefold)
print(missing_letter)

names = ["John",
         "Tim",
         "Bree",
         "Amanda",
         "Mikey"
         ]
names.sort(key=str.casefold)
print(names)