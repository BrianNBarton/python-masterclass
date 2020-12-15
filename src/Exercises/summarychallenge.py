# choice = "-"
# while choice != "0":
#     if choice in "12345":
#         print("you chose {}".format(choice))
#     else:
#         print("please choose your options from the list below")
#         print("1: \t learn python")
#         print("2: \t learn java")
#         print("3: \t go swimminmg")
#         print("4: \t have dinner")
#         print("5: \t go to bed")
#         print("0: \t exit")
#
#     choice = input()

for x in range(30):
    if x % 3 != 0 and x % 5 != 0:
        print(x)