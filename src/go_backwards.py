data = [105, 104, 4, 308, 3, 5,
        108, 100, 306, 108, 120, 160]

min_valid = 100
max_valid = 200

# for index in range(len(data) -1, -1, -1):
#     if data[index] < min_valid or data[index] > max_valid:
#         print(index, data)
#         del data[index]
top_index = len(data) - 1
for index, value in enumerate(reversed(data)):
    if value < min_valid or value > max_valid:
        print(top_index - index, value)
        del data[top_index - index]
#         shows values and position to be removed, and the list minus those values
