
import random
# generate a random number within this range
highest = 10
lowest = 0
answer = random.randint(1, highest)
print(answer)
# remove after testing
guess = 0

print("please guess a number between 1 and {}: ".format(highest))

while guess != answer:
    guess = int(input())

    if guess == 00:
        print("bye dude")

    if guess > highest:
        print("WITHIN range please.")

    if guess < lowest:
        print("that doesnt count dude")

    if guess == answer:
        print("well done you got it!")
    else:

        if guess < answer:
            print("that number is too low, try again")
        else:  # this must be greater than answer
            print("that number is too high, try again")



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
