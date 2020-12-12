
import random
# generate a random number within this range
highest = 10
answer = random.randint(1, highest)


print("please guess a number between 1 and {}: ".format(highest))
print(answer)

guess = int(input())

while answer != guess:
    print

if guess == answer:
    print("you got it on the first try!")
else:
    if guess != answer:

    if guess < answer:
        print("that number is too low")
    else:  # this must be greater than answer
        print("that number is too high")
    guess = int(input())
    if guess == answer:
        print("that is correct!")
    else:
        print("sorry, that is not correct")




#
# if guess < answer:
#     print("that number is too low")
#     guess = int(input())
#     if guess == answer:
#         print("well done, you guessed it!")
#     else:
#         print("sorry, you have not guessed correctly")
# elif guess > answer:
#     print("that number is too high")
#     guess = int(input())
#     if guess == answer:
#         print("well done, you guessed it!")
#     else:
#         print("sorry, you have not guessed correctly")
# else:
#     print("first try!!!")
#
#
#
#
# #
# # x = 5
# # y = 7
# #
# # if x > y:
# #     print("x is greater than y")
# # elif x < y:
# #     print("x is smaller than y")
# # else:
# #     print("x equals y")
