low = 1
high = 1000

print("please print a number between {} and {}".format(low, high))
print("press ENTER to continue")

guesses = 1
while low != high:
    # print("\tguessing in the range of {} to {} ".format(low, high))
    guess = low + (high - low) // 2
    high_low = input("my guess is {}. Should i guess higher or lower?"
                     " enter h, l, or c if my guess was correct "
                     .format(guess)).casefold()

    if high_low == "h":
        # guess higher
        low = guess + 1
    elif high_low == "l":
         # guess lower
         high = guess -1
    elif high_low == "c":
        print("you thought of the number {}".format(low))
        print("I got it in {} guesses!".format(guesses))
        break
    else:
        print("please print h, l, or c")

    guesses += 1
else:
    print("you thought of the number {}".format(low))
    print("i got it in {} guesses".format(guesses))

