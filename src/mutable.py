shopping_list = ["milk",
                  "eggs",
                  "bread",
                  "bacon",
                  "rice"
                 ]

another_list = shopping_list
print(id(shopping_list))
print(id(another_list))

shopping_list += ["cookies"]
print(shopping_list)
print(id(shopping_list))

print(another_list)

a = b = c = d = e = f = another_list
# chaining assignments this way is the same as the following
#
# a = another_list
# b = another_list
# c = another_list
# d = another_list
# e = another_list
# f = another_list
print(a)

print("adding cream")
b.append("cream")
print(c)
print(d)