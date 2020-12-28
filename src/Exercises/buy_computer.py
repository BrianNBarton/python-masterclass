available_parts = ["computer",
                   "monitor",
                   "keyboard",
                   "mouse",
                   "mouse pad",
                   "hdmi cable",
                   "dvd drive",
                   ]

# valid_choices = [str(i) for i in range(1, len(available_parts)+1)]
valid_choices = [str(i) for i in range(1, len(available_parts) + 1)]
print(valid_choices)
current_choice = "-"
computer_parts = []
# creates empty list

while current_choice != '0':
    if current_choice in valid_choices:
        index = int(current_choice) - 1
        chosen_part = available_parts[index]
        if chosen_part in computer_parts:
            print("removing {}".format(current_choice))
            computer_parts.remove(chosen_part)
        else:
            print("Adding {}".format(current_choice))
            computer_parts.append(chosen_part)
        print("your list now contains: {} ".format(computer_parts))
    else:
        print("please add options from the list below: ")
        for number, part in enumerate(available_parts):
            print("{0}: {1} ".format(number + 1, part))

    current_choice = input()

print(computer_parts)
