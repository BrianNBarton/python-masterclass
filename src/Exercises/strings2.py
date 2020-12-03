from operator import contains

parrot = "Norwegian Blue"

print(parrot)

# prints the given character, position 3 counting from 0
print(parrot[3])
print()
# we win vertical
print(parrot[3])
print(parrot[4])
print()
print(parrot[3])
print(parrot[6])
print(parrot[8])

# two of these come out the same way
meal1 = "spam" + "eggs" + "beans"
meal2 = "spam\neggs\nbeans"
meal3 = "spam, eggs, beans"
meal4 = """spam 
eggs 
beans"""

print(meal1)
print(meal2)
print(meal3)
print(meal4)


days = "Mon, Tue, Wed, Thu, Fri, Sat, Sun"
print(days[::5])


# Given the string



flower = "blue violet"

print(flower == 'blue')
print('blue' in flower)

a = 45
b = 15
c = 3

print(a - b / c)


quantity = 10
price = 5.0
total = quantity * price
tax = total / 5

Total = total + tax


print(total)

data = "1:A, 2:B, 3:C, 4:D, 5:E, 6:F, 7:G, 8:H"



# we want to slice the string to extract just the digits.

# Which of these slices will NOT do what we want?

#print(data[::5])
 # print(data[1:5]) this one
# print(data[0:-1:5])
#print(data[:-1:5])
