#
# for i in range(51):
#     if i % 3 == 0 and i % 5 == 0:
#         print("{} fizzbuzz".format(i))
#         continue
#     elif i % 3 == 0:
#         print("{} fizz".format(i))
#         continue
#     elif i % 5 == 0:
#         print("{} buzz".format(i))
#         continue
#     print("{} fizzbuzz".format(i))

for num in range(1, 21):
    if num % 3 == 0 and num % 5 == 0:
        print('{} FizzBuzz'.format(num))
    elif num % 3 == 0:
        print('{} Fizz'.format(num))
    elif num % 5 == 0:
        print('{} Buzz'.format(num))
    else:
        print(num)
