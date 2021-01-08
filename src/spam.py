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

for meal in menu:
    if "spam" not in meal:
        print(meal)
