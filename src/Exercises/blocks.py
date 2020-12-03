
name = input("please enter your name: ")
age = int(input("how old are you {0}? ".format(name)))
print(age)
if age >= 18:
    print("you are old enough to vote")
else:
    print("please come back in {0} years",format(18 - age))

#
# for i in range(1, 13):
#     print("No. {} squared is {} and cubed is {:4}".format(i, i ** 2, i ** 3))
#     print("-" * 50)



# I found a list of parts needed to build an affordable and styleish coffee table .
# I needed to calculate the total cost


# Here is the table of parts. Remove comments to test.

# 8 Pipes	90˚ Elbow Fitting	$1.66
# 4 Pipes	T Fitting	$2.51
# 4 Pipes	10” Nipple	$4.50
# 12 Pipes	12” Nipple	$5.25
# 4 Pipes	End Caps	$1.50\\


# Elbows = 1.66 * 8
# TFit = 2.51 * 4
# Nip1 = 4.50 * 4
# Nip2 = 5.25 * 12
# Endp = 1.50 * 4
#
# print(Elbows + TFit + Nip1 + Nip2 + Endp)
