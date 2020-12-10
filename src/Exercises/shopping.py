shopping_list = ["milk", "pasta", "chicken", "bred", "broccoli"]

# for item in shopping_list:
#     if item != "bred":
#         print("buy " + item)

# for item in shopping_list:
#     if item == "bred":
#         continue
#     print("buy " + item)

item_to_find = "breed"
found_at = None

for index in range(len(shopping_list)):
    if shopping_list[index] == item_to_find:
        found_at = index
        break
print("item found at position {}".format(found_at))
