
user_input = input(int("Enter a number between 0 and 1000: "))


if user_input.isdigit() and 0 <= int(user_input) <= 1000:
    formatted_number = user_input.zfill(6)
    print("Formatted number:", formatted_number)
else:
    print("Please enter a valid number between 0 and 1000.")



