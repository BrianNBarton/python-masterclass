# basic stuff

a = 12
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)

print()
# basic python for loop
for i in range(1, a // b):
    print(i)


# same output as for loop
i = 1
print(i)
i = 2
print(i)
i = 3
print(i)

# integer division, customers want whole buns, not part of a bun, they have 15 dollars
bun_price = 2.40
money = 15

print(money // bun_price)

# order of operations pemdas example

print(a + b / 3 - 4 + 12)
print(a + (b / 3) - (4 * 12))
# The above should have the same output (-35)

print(((( a + b ) / 3 ) -4 ) * 12)
print(((a + b) / 3 - 4 ) * 12)
# The above should have the same output (12)

# multiplying and dividing have a higher precedence than adding and subtracting.

c = a + b
d = c / 3
e = d - 4
print(e * 12)
# same output as above (12)

print()
print(a / (b * a) / b)