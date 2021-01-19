menu = [
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["eggs", "bacon"],
    ["eggs", "sausage", "bacon"],
    ["eggs", "spam"],
    ["eggs", "bacon", "spam"],
    ["eggs", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "eggs", "spam", "spam", "bacon", "spam"]
]

# for meal in menu:
#     for index in range(len(meal) -1, -1, -1):
#         if meal[index] == "spam":
#             del meal[index]
#
#         print(meal)

for meal in menu:
    for item in meal:
        if item != "spam":
            print(item, end=" ")
    print()
