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